with open('./22/input_a.txt') as f:
    input = [int(a.strip()) for a in f if ':' not in a and not a.strip() == '']
    
def hash(p1, p2, sep = 1):
    return sum([(len(p1) + len(p2)*sep - i) * a for i,a in enumerate(p2 + p1)])

def playGame(p1, p2, game, recurse = False):
    history = []
    while len(p1) > 0 and len(p2) > 0:
        if recurse and hash(p1,p2,1000) in history: return True
        history.append(hash(p1,p2,1000))
        c1, c2 = p1[0], p2[0]
        p1Wins = c1 > c2
        if recurse and len(p1) > c1 and len(p2) > c2:
            p1Wins = playGame(p1[1:c1+1], p2[1:c2+1], game + 1, True)
        if p1Wins: p1.extend([c1, c2])
        else: p2.extend([c2, c1])
        p1, p2 = p1[1:], p2[1:]
    return len(p1) > 0 if game > 1 else hash(p1, p2)

p1, p2 = input[:len(input)//2], input[len(input)//2:]
print(f'Part A: sum of cards = {playGame(p1, p2, 1, False)}')

p1, p2 = input[:len(input)//2], input[len(input)//2:]
print(f'Part B: sum of cards = {playGame(p1, p2, 1, True)}')