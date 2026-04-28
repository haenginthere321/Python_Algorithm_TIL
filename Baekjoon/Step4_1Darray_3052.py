li,c = [], []

for i in range(10):
    a = int(input())
    li.append(a%42)
for j in li:
    if j in c:
        continue
    c.append(j)

print(len(c))
