with open('./15/input_a.txt', 'r') as f:
    input = [int(a) for a in f.readline().strip().split(',')]

def playGame(seed : list, limit : int):
    mem, i, last = dict(), len(seed)+1, input[len(seed)-1]
    for a, num in enumerate(seed[:-1]): mem[num] = a+1
    while i < limit + 1:
        num = 0 if last not in mem else i-1 - mem[last]
        mem[last] = i-1
        last = num
        i += 1
    return last

print(f'Part A: score after 2020 turns: {playGame(input, 2020)}')
print(f'Part B: score after 30m turns: {playGame(input, 30000000)}')