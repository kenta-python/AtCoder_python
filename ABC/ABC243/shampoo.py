v, a, b, c = map(int, input().split())

x = v%(a+b+c)
if x < a:
  print('F')
elif a <= x < a+b:
  print('M')
else:
  print('T')