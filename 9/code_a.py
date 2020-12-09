input = []
with open('./9/input_a.txt', 'r') as f:
    for line in f: input.append(int(line.strip()))

# Not the worlds most beautiful code but gets the job done at 7am :)
preamble = 25
weak = 0
for i in range(preamble,len(input)-1):
    weak = input[i]
    matched = False
    for j in range(i-preamble,i):
        for k in range(i-preamble,i):
            if weak == input[j] + input[k] and input[j] != input[k]:
                matched = True
    if matched == False:
        print(f'Part A: first invalid # {weak}')
        break

for i in range(preamble,len(input)-1):
    sum = 0
    j = i
    minB = 9999999999999
    maxB = 0

    while sum < weak:
        sum += input[j]
        minB = min(minB, input[j])
        maxB = max(maxB, input[j])
        j += 1
    
    if sum == weak:
        print(f'Part B: key = {minB+maxB}')
        break