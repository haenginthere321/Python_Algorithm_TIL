arr = [list(map(int,input().split())) for i in range(9)]
c = 0
n,m = 0,0

for i in range(9):
  for j in range(9):
    if arr[i][j] > c:
      c = arr[i][j]
      n,m = i,j

print(c)
print(n+1,m+1)
