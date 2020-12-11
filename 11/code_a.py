with open('./11/input_a.txt', 'r') as f:
    input = [list(line.strip()) for line in f]

def numAdjOccupied(seating, row, seat):
    occupied = 0
    for r in range(row-1,row+2):
        for s in range(seat-1, seat+2):
            if (r == row and s == seat) or r < 0 or s < 0 or r >= len(seating) or s >= len(seating[0]):
                continue
            elif seating[r][s] == '#': occupied += 1
    return occupied

def findSeatOcc(seating, rowMove, seatMove, rowStart, seatStart):
    r = rowStart + rowMove
    s = seatStart + seatMove
    if rowMove == 0 and seatMove == 0: return 0
    while not(r < 0 or s < 0 or r >= len(seating) or s >= len(seating[0])):
        if seating[r][s] == '#': return 1
        if seating[r][s] == 'L': return 0
        r += rowMove
        s += seatMove
    return 0

def numProjectedOccupied(seating, row, seat):
    if seating[row][seat] == '.': return 0
    occupied = 0
    for r in range(-1,2):
        for s in range(-1, 2):
            occupied += findSeatOcc(seating, r, s, row, seat)
    return occupied

def applyRules(seating, func, tolerance):
    newSeating = []
    changes = 0
    for r in range(0, len(seating)):
        newSeating.append([])
        for s in range(0, len(seating[0])):
            seat = seating[r][s]
            occ = func(seating,r,s)
            changes += 1
            if seat == 'L' and occ == 0: newSeating[r].append('#')
            elif seat == '#' and occ >= tolerance: newSeating[r].append('L')
            else: 
                newSeating[r].append(seating[r][s])
                changes -= 1
    return newSeating, changes

def countOcc(seating):
    numOccupied = 0
    for r in seating:
        for s in r:
            if s == '#': numOccupied += 1
    return numOccupied

changes = 1
limit = 1000
i = 0
seating = input
while changes > 0 and i < limit:
    seating, changes = applyRules(seating, numAdjOccupied, 4)
    i += 1

print(f'Part A: {countOcc(seating)} seats occupied in {i} iterations')

changes = 1
i = 0
seating = input
while changes > 0 and i < limit:
    seating, changes = applyRules(seating, numProjectedOccupied, 5)
    i += 1

print(f'Part B: {countOcc(seating)} seats occupied in {i} iterations')