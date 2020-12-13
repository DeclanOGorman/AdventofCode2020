import math

with open('./13/input_a.txt', 'r') as f:
    timestamp = int(f.readline().strip())
    busses = [(i, int(a)) for i, a in enumerate(f.readline().strip().split(',')) if a != 'x']

nextBus, arrival = 0, 999
for bus in busses:
    if bus == 1: continue
    time = bus - (timestamp % bus)
    if time < arrival:
        arrival = time
        nextBus = bus

print(f'Part A: next bus: {nextBus} in {arrival} = {nextBus * arrival}')

product, timestamp = 1, 0
for delta, bus in busses:
    while True:
        if (delta + timestamp) % bus == 0: break
        timestamp += product
    product *= bus

print(f'Part B: timestamp = {timestamp}')
