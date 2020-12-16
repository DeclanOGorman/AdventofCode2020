import re

with open('./16/input_a.txt', 'r') as f:
    input = [a.strip() for a in f]

rulesRe = r'^([a-z\s]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)$'
ticketRe = '^(\d+)(,\d+)*$'

rules = []
for rraw in [a for a in input if re.match(rulesRe, a)]:
    rule = []
    r = rraw.split(': ')[1].split(' or ')
    rule.append(rraw.split(': ')[0])
    rule.append(int(r[0].split('-')[0]))
    rule.append(int(r[0].split('-')[1]))
    rule.append(int(r[1].split('-')[0]))
    rule.append(int(r[1].split('-')[1])) 
    rules.append(rule)
tickets = [a.split(',') for a in input if re.match(ticketRe, a)]

ruleset = dict()
for r in range(0,len(tickets[0])):
    ruleset[r] = [a[0] for a in rules]

sumInvalid = 0
validTickets = []
for t in tickets[1:]:
    valid = True
    for fstr in t:
        matched = False
        f = int(fstr)
        for r in rules:
            if f >= r[1] and f <= r[2] or f >= r[3] and f <= r[4]: matched = True
        if not matched:
            valid = False 
            sumInvalid += f
    
    if valid:
        validTickets.append(t)

print(f'Part A: invalid fields = {sumInvalid}')

for t in validTickets:
    for i, fstr in enumerate(t):
        f = int(fstr)
        for r in rules:
            if not(f >= r[1] and f <= r[2] or f >= r[3] and f <= r[4]):
                ruleset[i].remove(r[0])

found = True
for i in range(0,100):
    for r in ruleset:
        if len(ruleset[r]) == 1:
            for r2 in ruleset:
                if len(ruleset[r2]) > 1 and ruleset[r][0] in ruleset[r2]:
                    ruleset[r2].remove(ruleset[r][0])

sumdepartures = 1
for i, f in enumerate(tickets[0]):
    if ruleset[i][0].startswith('departure'):
        sumdepartures *= int(f)

print(f'Part B: sum of depature fields = {sumdepartures}')