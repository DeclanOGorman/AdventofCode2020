with open('./21/input_a.txt','r') as f:
    input = [a.strip().replace(')','').split(' (contains ') for a in f]

alg, globIng, alIng = dict(), list(), set()
for f in input:
    ing = set(f[0].split())
    globIng = globIng + list(ing)
    for a in f[1].split(', '):
        if not a in alg: alg[a] = ing.copy()
        else: alg[a] &= ing

for i in range(0, len(alg)):
    for a in alg:
        if len(alg[a]) == 1:
            alIng = alIng.union(alg[a])
            for a2 in alg:
                if not a2 == a: alg[a2] -= alg[a]

safeIng = [i for i in globIng if i not in alIng]
print(f'Part A: num safe ingredients - {len(safeIng)}')

sortedAlIng = list(alg)
sortedAlIng.sort()
output = ','.join([list(alg[i])[0] for i in sortedAlIng])
print(f'Part B: Sorted = {output}')