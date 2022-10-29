a, b, c, x = map(int, input().split())

if a >= x:
  print(float(1))
elif b < x:
  print(float(0))
else:
  print(c/(b-a))