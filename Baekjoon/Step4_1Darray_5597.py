li = []
for i in range(28):
    li.append(int(input()))
li.sort()
for j in range(1,31):
    if j not in li:
        print(j)
