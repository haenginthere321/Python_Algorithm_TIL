word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
c, i = 0, 0

while i < len(word):
    if word[i:i+3] in croatia:
        c += 1
        i += 3
    elif word[i:i+2] in croatia:
        c += 1
        i += 2
    else:
        c += 1
        i += 1
print(c)
