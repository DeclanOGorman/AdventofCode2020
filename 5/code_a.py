def getSeat(lower, upper, ticket):
    if len(ticket) == 0: return int(lower)
    elif ticket[0] == 'F' or ticket[0] == 'L': 
        return getSeat(lower, lower + ((upper-lower)/2), ticket[1:])
    else: 
        return getSeat(lower + ((upper-lower)/2), upper, ticket[1:]) 

input = []
with open('./5/input_a.txt', 'r') as f:
    for line in f: input.append(line.strip())

seats = {}
for ticket in input:
    row = getSeat(0, 128, ticket[0:7])
    seat = getSeat(0,8, ticket[7:])
    seats[row * 8 + seat] = 1

missingSeat = lambda i: i not in seats and i - 1 in seats and i + 1 in seats
seat = list(filter(missingSeat, range(1, max(seats))))[0]

print(f'Part A: max seat number: {max(seats)}')
print(f'Part B: missing seat number: {seat}')