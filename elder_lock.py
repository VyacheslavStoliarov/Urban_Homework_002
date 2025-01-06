import random
one_stone = random.randrange(3, 21)
print(f'[-*[\033[33m{one_stone}\033[0m]*-]')
for i in range(1, one_stone//2 + 1):
    for j in range(i + 1, one_stone):
        if one_stone % (i + j) == 0:
            print(f'[{i},{j}]', end = '')