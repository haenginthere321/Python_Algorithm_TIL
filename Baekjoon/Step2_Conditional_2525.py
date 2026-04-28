a,b = map(int,input().split())
c = int(input())
if 0 <= a <= 23 and (b+c) < 60:
  print(a,b+c)
elif a == 23 and (b+c) > 60:
  print(a-23,(b+c)-35)
elif 0 < a < 23 and (b+c) > 60:
  print(a+1,(b+c)-35)

a = a%23
b = b%60
