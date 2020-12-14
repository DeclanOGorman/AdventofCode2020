def applyMask(value : int, mask):
    b = list(format(value, '036b'))
    m = [str(b[i]) if mask[i] == 'X' else mask[i] for i in range(0, len(mask))]
    return int(''.join(m),2)

def applyFloatingMask(value : int, mask):
    b = list(format(value, '036b'))
    template, map, out = [], [], []
    for i in range(0, len(mask)):
        if mask[i] == '0': template.append(str(b[i]))
        elif mask[i] == '1': template.append('1')
        else:
            template.append('0')
            map.append(i)

    for i in range(0, 2**len(map)):
        b = list(format(i, f'0{len(map)}b'))
        for j in range(0, len(map)):
            template[map[j]] = b[j]
        out.append(int(''.join(template),2))
        
    return out

with open('./14/input_a.txt', 'r') as f:
    input = [line.strip().split(' = ') for line in f]

mask = list('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
mem = dict()
for instr in input:
    if instr[0] == 'mask': mask = instr[1]
    elif instr[0][:3] == 'mem':
        loc = int(instr[0].replace(']','[').split('[')[1])
        mem[loc] = applyMask(int(instr[1]), mask)

print(f'Part A: {sum(mem.values())}')

mem = dict()
for instr in input:
    if instr[0] == 'mask': mask = instr[1]
    elif instr[0][:3] == 'mem':
        loc = int(instr[0].replace(']','[').split('[')[1])
        locs = applyFloatingMask(loc, mask)
        for loc in locs:
            mem[loc] = int(instr[1])

print(f'Part B: {sum(mem.values())}')