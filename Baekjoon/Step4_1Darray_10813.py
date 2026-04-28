N, M = map(int,input().split())
li = []
for i in range(1,N+1):
    li.append(i)
for i in range(M):
    c = 0
    a,b = map(int,input().split())
    c = li[a-1]
    li[a-1] = li[b-1]
    li[b-1] = c


print(*li,end=' ')
