n = int(input())
scores = list(map(int,input().split()))
m = max(scores)

avr = sum(scores) / m * 100 / n
print(avr)
