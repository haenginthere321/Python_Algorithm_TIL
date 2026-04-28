N, M = map(int,input().split())
li = [0]*N
for p in range(M):
    i, j, k = map(int,input().split())
    for b in range(i-1,j):
        li[b] = k

print(*li)
