n = input()
c = 0

for i in range(len(n)):
    if n[i] in ['A', 'B', 'C']:
        c += 3
    elif n[i] in ['D', 'E', 'F']:
        c += 4
    elif n[i] in ['G', 'H', 'I']:
        c += 5
    elif n[i] in ['J', 'K', 'L']:
        c += 6
    elif n[i] in ['M', 'N', 'O']:
        c += 7
    elif n[i] in ['P', 'Q', 'R', 'S']:
        c += 8
    elif n[i] in ['T', 'U', 'V']:
        c += 9
    else:
        c += 10

print(c)
