def expandBranch(rules, bagsFound, bag, num = 1):
    bagsFound.append(bag)
    val = num
    for rule in rules[bag]:
        val += expandBranch(rules,bagsFound, rule[0], num * rule[1])
    return val

input = []
with open('./7/input_a.txt', 'r') as f:
    for line in f: input.append(line.strip())

rules = dict()
for rule in input:
    bag = rule.split(' contain ')[0].replace('bags','bag')
    rules[bag] = []
    if rule.split(' contain ')[1] != 'no other bags.':
        for bagsIn in rule.split(' contain ')[1][:-1].split(', '):
            rules[bag].append([bagsIn[2:].replace('bags','bag'), int(bagsIn[0])])


testA = 'shiny gold bag'
numA = 0
for start in rules:
    bagsFound = []
    expandBranch(rules, bagsFound, start)
    if testA in bagsFound[1:]: numA += 1

numB = expandBranch(rules, [], testA) - 1

print(f'Part A: {numA} of bags can contain a {testA}')
print(f'Part B: {numB} of bags in a {testA}')
