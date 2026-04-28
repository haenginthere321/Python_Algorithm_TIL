N, X = map(int,input().split())
A = list(map(int,input().split()))
l = []
for i in A:
    if i < X:
        l.append(i)

print(*l,sep=' ')
