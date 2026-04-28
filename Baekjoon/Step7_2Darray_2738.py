n,m = map(int,input().split())
a = [list(map(int,input().split())) for i in range(n)]
b = [list(map(int,input().split())) for i in range(n)]
c = [[0]*m for i in range(n)]

for i in range(n):
  for j in range(m):
    c[i][j] = a[i][j] + b[i][j]

for i in c:
  print(*i)
