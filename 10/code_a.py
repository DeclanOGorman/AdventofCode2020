with open('./10/input_a.txt', 'r') as f:
    input = [int(line.strip()) for line in f]

input.sort()
diff = [0,0,0,0]
joltage = 0
for j in input:
    diff[j-joltage] += 1
    joltage = j
diff[3] += 1

print(f'Part A: {diff[1]*diff[3]}')

input.append(0)
input.sort()

def splitThrees(adapters):
    splitInput = [[]]
    last = 0
    for i in adapters:
        if i == last + 3: splitInput.append([i])
        else: splitInput[len(splitInput)-1].append(i)
        last = i
    return splitInput

def seq(adapters, index):
    paths = 0
    i = index + 1
    length = len(adapters)
    if (i == length): return 1
    while i < length and adapters[i] <= adapters[index] + 3:
        paths += seq(adapters, i)
        i = i+1
    return paths

total = 1
for s in splitThrees(input):
    total *= seq(s,0)

print(f'Part B: {total}')