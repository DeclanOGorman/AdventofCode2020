with open('./17/input_a.txt', 'r') as f:
    input = [list(a.strip()) for a in f]

cycles = 6
gridWidth = cycles * 2 + len(input)

def hash(x,y,z,w = 0): return x + y*gridWidth + z*(gridWidth**2) + w*(gridWidth**3)
def unhash(hash): 
    x = hash % gridWidth
    w = int(hash / gridWidth**3)
    z = int((hash - x - w*gridWidth**3) / gridWidth**2)
    y = int((hash - x - w*gridWidth**3 - z*gridWidth**2) /gridWidth)
    return x, y, z, w

def newState(grid, inactive, h, is4d = False):
    x,y,z,w = unhash(h)    
    neighboursOn = 0
    for xdiff in range(x-1, x+2):
        for ydiff in range(y-1, y+2):
            for zdiff in range(z-1, z+2):
                for wdiff in range(w-1, w+2) if is4d else [0]:
                    if xdiff == x and ydiff == y and zdiff == z and wdiff == w: continue
                    n = hash(xdiff,ydiff,zdiff,wdiff)
                    if n in grid: neighboursOn += 1
                    else: 
                        if n in inactive: inactive[n] += 1
                        else: inactive[n] = 1
    return True if neighboursOn == 2 or neighboursOn == 3 else False    

gridInput = dict()
for i, x in enumerate(input):
    for j, y in enumerate(x):
        if y == '#': gridInput[hash(i,j,0,0)] = True

grid = gridInput.copy()
for c in range(1,cycles+1):
    newGrid = dict()
    inactive = dict()
    for cube in grid:
        if newState(grid, inactive, cube): 
            newGrid[cube] = True

    for inactivecubes in inactive:
        if inactive[inactivecubes] == 3: newGrid[inactivecubes] = True
    grid = newGrid

print(f'Part A: Number of on cubes: {len(grid)}')

grid = gridInput
for c in range(1,cycles+1):
    newGrid = dict()
    inactive = dict()
    for cube in grid:
        if newState(grid, inactive, cube, True): 
            newGrid[cube] = True

    for inactivecubes in inactive:
        if inactive[inactivecubes] == 3: newGrid[inactivecubes] = True
    grid = newGrid

print(f'Part B: Number of on cubes in 4d: {len(grid)}')