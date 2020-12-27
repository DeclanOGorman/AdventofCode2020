with open('./25/input_a.txt', 'r') as f:
    card, door = [int(a.strip()) for a in f]

cardLoop, doorLoop, mod = 0, 0, 20201227
for i in range(100000000):
    val = pow(7, i, mod)
    if val == card: cardLoop = i
    if val == door: doorLoop = i
    if cardLoop > 0 and doorLoop > 0: break

enc = pow(card, doorLoop, mod)
print(f'Part A: Card loop = {cardLoop}, door loop = {doorLoop}, encryptionKey = {enc}')
