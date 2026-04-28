a, b = int(input()), int(input())
c = [list(map(int,input().split())) for i in range(b)]
d = 0

for i in c:
  d += (i[0] * i[1])
if d == a:
  print("Yes")
else:
  print("No")
