s = input()
li = []
for i in range(97,123):
    if chr(i) in s:
        li.append(s.index(chr(i)))
    else:
        li.append(-1)
print(*li)
