a = int(input())
b = [list(map(int,input().split())) for i in range(a)]

for i in b:
  print(i[0] + i[1])
