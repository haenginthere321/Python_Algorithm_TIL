a = [list(input()) for i in range(5)]
b = [['10']*15 for i in range(5)]

for i in range(len(a)):
  for j in range(len(a[i])):
    b[i][j] = a[i][j]

s = ''

for i in range(15):
  for j in range(5):
    if b[j][i] != '10':
      s += b[j][i]

print(s)
