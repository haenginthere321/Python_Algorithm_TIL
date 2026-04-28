n = int(input())
for _ in range(n):
    i, j = input().split()
    for k in j:
        print(k*int(i),end='')
    print()
