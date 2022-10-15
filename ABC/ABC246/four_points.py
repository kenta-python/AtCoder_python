x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

def solve(x1, x2, x3):
  if x1 == x2:
    xans = x3
  elif x1 == x3:
    xans = x2
  else:
    xans = x1
  return xans

print(solve(x1, x2, x3), solve(y1, y2, y3))