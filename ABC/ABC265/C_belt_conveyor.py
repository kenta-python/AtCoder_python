def solve():
  h, w = map(int, input().split())
  g = [input() for _ in range(h)]
  seen = [[False]*w for _ in range(h)]
  x, y = 0, 0
  while True:
    seen[x][y] = True
    if g[x][y] == 'U':
      cx, cy = x-1, y
    elif g[x][y] == 'D':
      cx, cy = x+1, y
    elif g[x][y] == 'L':
      cx, cy = x, y-1
    elif g[x][y] == 'R':
      cx, cy = x, y+1
    if not ((0<= cx < h) and (0<= cy < w)):
      return x+1, y+1
    if seen[cx][cy]:
      return (-1,)
    x, y = cx, cy

print(*solve())