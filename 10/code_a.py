input = []
with open('./10/input_b_test.txt', 'r') as f:
    for line in f: input.append(int(line.strip()))

input.sort()
diff = [0,0,0,0]
joltage = 0
for j in input:
    diff[j-joltage] += 1
    joltage = j
diff[3] += 1

print(f'Part A: {diff[1]*diff[3]}')

def seq(adapters, joltage):
    a = list(filter(lambda c: c > joltage and c <= joltage + 3, adapters))
    paths = 0
    for j in a:
        paths += seq(list(filter(lambda b: b > j, adapters)), j)
    if len(a) == 0: 
        return 1
    return paths

length = len(input)
def seq2(adapters, index):
    paths = 0
    i = index + 1
    if (i == length): return 1
    while adapters[i] <= adapters[index] + 3:
        paths += seq2(adapters, i)
        i = i+1
        if (i == length): return 1
    return paths

print(f'Part B: {seq2(input,0)}')