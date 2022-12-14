a, b, c = map(int, input().split())
if a == b and b == c:
  print(a)
elif (a == b and b != c):
  print(c)
elif (a == c and b != c):
  print(b)
elif (b == c and a != c):
  print(a)
else:
  print(0)