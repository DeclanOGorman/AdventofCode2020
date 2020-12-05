def getSeat(lower, upper, ticket):
    if ticket[0] == 'F' or ticket[0] == 'L': upper = lower + ((upper-lower)/2)
    else: lower = lower + ((upper-lower)/2)

    if len(ticket) == 1: return int(lower)
    else: return getSeat(lower, upper, ticket[1:])

input = []
with open('./5/input_a.txt', 'r') as f:
    for line in f: input.append(line.strip())

seats = {}
for ticket in input:
    row = getSeat(0, 128, ticket[0:7])
    seat = getSeat(0,8, ticket[7:])
    seats[row * 8 + seat] = 1

seat = 0
for i in range(1,max(seats)):
    if i not in seats and i - 1 in seats and i + 1 in seats:
        seat = i

print(f'Part A: max seat number: {max(seats)}')
print(f'Part B: missing seat number: {seat}')