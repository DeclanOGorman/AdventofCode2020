with open('./19/input_a.txt', 'r') as f:
    input = [a.strip().replace('"','') for a in f if a.strip() != '']
    input_rules = {a.split(':')[0] : a.split(':')[1].split('|') for a in input if ':' in a}
    input_sets = [a for a in input if not ':' in a]

def expandTree(tree : dict, start : int, depth : int = 0):
    rrules = []
    for branch in tree[start]:
        rules = ['']
        for elem in branch.strip().split(' '):
            if elem in ['a', 'b']: 
                rules = [r + elem for r in rules]
            else:
                subrules = expandTree(tree, elem)
                trules = []
                for sr in subrules:
                    for r in rules:
                        trules.append(r + sr)
                rules = trules
        rrules += rules
    return rrules

rules = expandTree(input_rules, '0')
tot = sum([1 if a in rules else 0 for a in input_sets])
print(f'Part A: num matching = {tot}')

input_rules['8'] = ['12','42 8']
input_rules['11'] = ['42 31','42 11 31']

rules = expandTree(input_rules, '0')
tot = sum([1 if a in rules else 0 for a in input_sets])
print(f'Part B: num matching = {tot}')