h, w, x, y = map(int, input().split())
x -= 1
y -= 1
grid = [input() for _ in range(h)]

ans = 1

for i in reversed(range(x)):
  if grid[i][y] == '#':
    break
  else:
    ans += 1

for i in range(x+1, h):
  if grid[i][y] == '#':
    break
  else:
    ans += 1

for i in reversed(range(y)):
  if grid[x][i] == '#':
    break
  else:
    ans += 1

for i in range(y+1, w):
  if grid[x][i] == '#':
    break
  else:
    ans += 1

print(ans)
  