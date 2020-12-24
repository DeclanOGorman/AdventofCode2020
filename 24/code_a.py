import re

with open('./24/input_a.txt', 'r') as f:
    input = [re.findall('(w|e|se|sw|ne|nw)', a.strip()) for a in f]

def hash(x, y): return x + y * 1000
def unhash(hash): return hash % 1000, hash // 1000

dirs = {'w': [-1,0], 'e': [1,0], 'se': [0,-1], 'sw': [-1,-1], 'ne': [1,1], 'nw': [0,1]}
grid = dict()
for d in input:
    x, y = 0, 0
    for m in d:
        x += dirs[m][0]
        y += dirs[m][1]
    grid[hash(x,y)] = True if hash(x,y) not in grid else not grid[hash(x,y)]

print(f'Part A: Black tiles = {sum([1 if grid[a] == True else 0 for a in grid])}') 
    
def runDay(grid):
    newGrid = dict()
    whites = dict()
    for t in grid:
        if grid[t] == False: continue
        x, y = unhash(t)
        adjBlack = 0
        for d in dirs:
            tile = hash(x + dirs[d][0], y + dirs[d][1])
            if grid.get(tile, False) == True: adjBlack += 1
            else: whites[tile] = 1 + whites.get(tile, 0)
        if adjBlack == 1 or adjBlack == 2: newGrid[t] = True
    for w in whites:
        if whites[w] == 2: newGrid[w] = True
    return newGrid

for d in range(0, 100): grid = runDay(grid)
print(f'Part B: Black tiles = {sum([1 if grid[a] == True else 0 for a in grid])}')