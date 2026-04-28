li = list(input().split())
li[0], li[1] = int(li[0][::-1]), int(li[1][::-1])
print(max(li))
