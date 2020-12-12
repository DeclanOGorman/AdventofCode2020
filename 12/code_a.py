with open('./12/input_a.txt', 'r') as f:
    input = [[line.strip()[0], int(line.strip()[1:])] for line in f]

heading, eastWest, northSouth = 'E', 0, 0

compass = ['N','E','S','W']
directions = {'N': [1,0], 'E': [0,1], 'S': [-1,0], 'W': [0,-1]}

for nav in input:
    if nav[0] == 'R':
        heading = compass[int((compass.index(heading) + (nav[1] / 90)) % 4)]
        continue
    elif nav[0] == 'L':
        heading = compass[int((compass.index(heading) + (nav[1] / 90 * -1)) % 4)]
        continue
    elif nav[0] == 'F':
        dir = directions[heading]
    else:
        dir = directions[nav[0]]

    eastWest += dir[1]*nav[1]
    northSouth += dir[0]*nav[1]

print(f'Part A: coords: {northSouth}:{eastWest}, distance: {abs(northSouth) + abs(eastWest)}')

shipEastWest, shipNorthSouth, wpEastWest, wpNorthSouth = 0, 0, 10, 1
transpose = [[[1,0],[0,1]],[[0,-1],[1,0]],[[-1,0],[0,-1]],[[0,1],[-1,0]]]
#             0 deg / 360   L90 / R270      L180 / R180     L270 / R90

for nav in input:
    if nav[0] == 'R':
        trans = transpose[int(4-nav[1]/90)]
        oldEastWest = wpEastWest
        wpEastWest = wpNorthSouth * trans[0][1] + wpEastWest * trans[0][0]
        wpNorthSouth = wpNorthSouth * trans[1][1] + oldEastWest * trans[1][0]
        continue
    elif nav[0] == 'L':
        trans = transpose[int(nav[1]/90)]
        oldEastWest = wpEastWest
        wpEastWest = wpNorthSouth * trans[0][1] + wpEastWest * trans[0][0]
        wpNorthSouth = wpNorthSouth * trans[1][1] + oldEastWest * trans[1][0]
        continue
    elif nav[0] == 'F':
        shipEastWest += wpEastWest * nav[1]
        shipNorthSouth += wpNorthSouth * nav[1]
        continue
    else:
        dir = directions[nav[0]]

    wpEastWest += dir[1]*nav[1]
    wpNorthSouth += dir[0]*nav[1]

print(f'Part B: coords: {shipNorthSouth}:{shipEastWest}, distance: {abs(shipNorthSouth) + abs(shipEastWest)}')