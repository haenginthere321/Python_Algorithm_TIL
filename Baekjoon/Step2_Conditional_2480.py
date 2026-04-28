a,b,c = map(int,input().split())
if a == b == c:
  print(10000+(a*1000))
elif a == b and c != a:
  print(1000+(a*100))
elif a == c and b != c:
  print(1000+(a*100))
elif b == c and a != b:
  print(1000+(b*100))
else:
  if a < b and c < b:
    print(b*100)
  elif b < a and c < a:
    print(a*100)
  elif a < c and b < c:
    print(c*100)
