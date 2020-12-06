groups = []
with open('./6/input_a.txt', 'r') as f:
    input = []
    for line in f: 
        if line.strip() == '': 
            groups.append(input)
            input = []
        else: input.append(line.strip())
groups.append(input)

num = 0
for group in groups:
    num += len(''.join(set(''.join(group))))

print(f'Part A: {num}')

num = 0
for group in groups:
    num += len(set(group[0]).intersection(*group))

print(f'Part B: {num}')