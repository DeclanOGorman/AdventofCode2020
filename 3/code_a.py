# https://adventofcode.com/2020/day/3

def countTrees(grid,down,lateral,x,y):
    trees = 0
    while y < len(grid):
        if grid[y][x] == '#': trees += 1
        y += down
        x += lateral
        if x >= len(grid[0]): x -= len(grid[0])
    return trees

grid = []
with open('./3/input_a.txt', 'r') as f:
    for line in f: grid.append(list(line.strip()))

trees = countTrees(grid,1,3,0,0)
print(f'Part a: {trees} trees')

trees = 1
moves = [[1,1],[1,3],[1,5],[1,7],[2,1]]
for move in moves: trees *= countTrees(grid,move[0],move[1],0,0)
print(f'Part b: {trees} total trees')
