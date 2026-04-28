N = int(input())
n = list(map(int,input().split()))
v = int(input())
c = 0
for i in n:
    if i == v:
        c += 1
print(c)
