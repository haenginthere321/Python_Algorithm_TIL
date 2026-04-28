n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
arr = [[0]*100 for i in range(100)]
x,y = [],[]
z = 0

for i in range(len(a)):
  x.append(a[i][0])
  y.append(a[i][1])


for i in range(n):
  for j in range(100):
    if j == y[i]:
      c = 100 - y[i]
      b = x[i]
      for h in range(c-10,c):
        for v in range(b,b+10):
          arr[h][v] = 1

for i in range(len(arr)):
  for j in range(len(arr)):
    if arr[i][j] == 1:
      z += 1

print(z)
