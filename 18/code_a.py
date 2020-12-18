with open('./18/input_a.txt', 'r') as f:
    input = [a.strip().replace('(', '( ').replace(')',' )').split() for a in f]
    for a in input: a.reverse()

ops = ['+','-','*']

def eval(parts : list):
    total = 0
    operand = ''
    while len(parts) > 0:
        part = parts.pop()
        if part in ops: operand = part
        elif part == ')': return total
        else:
            if part == '(': part = eval(parts)
            if operand == '': total = int(part)
            elif operand == '*': total *= int(part)
            elif operand == '+': total += int(part)
            elif operand == '-': total -= int(part)
    return total

print(f'Part A: sum answers = {sum([eval(a) for a in input])}')

with open('./18/input_a.txt', 'r') as f:
    input = [a.strip() for a in f]

sumAll = 0
for a in input:
    eqn = '(((' + a.replace('(','(((').replace(')',')))').replace(' + ', ') + (').replace(' * ',')) * ((') + ')))'
    eqn = eqn.replace('(', '( ').replace(')',' )').split()
    eqn.reverse()
    sumAll += eval(eqn)

print(f'Part B: sum answers = {sumAll}')