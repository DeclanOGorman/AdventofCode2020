# https://adventofcode.com/2020/day/2

def isValidPasswordA(test, char, min, max):
    count = 0
    for letter in test:
        if letter == char: count += 1

    if count >= min and count <= max: return 1
    return 0

def isValidPasswordB(test, char, min, max):
    if test[min-1] == char and test[max-1] == char : return 0
    if test[min-1] == char or test[max-1] == char : return 1
    return 0

print('starting...')
input = []
with open('./2/input_a.txt', 'r') as f:
    for line in f: input.append(line.strip())

validPasswordsA = 0
validPasswordsB = 0
for password in input:
    temp = password.split(': ')
    test = temp[1]
    temp = temp[0].split()
    char = temp[1]
    temp = temp[0].split('-')
    min = int(temp[0])
    max = int(temp[1])
    validPasswordsA += isValidPasswordA(test, char, min, max)
    validPasswordsB += isValidPasswordB(test, char, min, max)

print(f'Part a: {validPasswordsA} valid passwords')
print(f'Part b: {validPasswordsB} valid passwords')
