def runProgram(code, ):
    line = 0
    acc = 0
    lines = [0]
    while line < len(input):
        if input[line][0] == 'acc': acc += int(input[line][1])
        elif input[line][0] == 'jmp': line += int(input[line][1]) - 1

        line += 1
        if line in lines: break
        else: lines.append(line)
    return acc, line >= len(input)

input = []
with open('./8/input_a.txt', 'r') as f:
    for line in f: input.append(line.strip().split())
    
print(f'Part A: output is {runProgram(input[0])[0]}')

acc = 0
for i in range(0, len(input)):
    cmd = input[i][0]
    if cmd == 'jmp': input[i][0] = 'nop'
    if cmd == 'nop': input[i][0] = 'jmp'
    output = runProgram(input)
    input[i][0] = cmd
    acc = output[0]
    if output[1]: break

print(f'Part B: fixed program output is {acc}')