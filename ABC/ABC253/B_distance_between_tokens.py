h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

a = []
for i in range(h):
  for j in range(w):
    if s[i][j] ==  'o':
      a.append([i, j])

ans = abs(a[0][0]-a[1][0]) + abs(a[0][1]-a[1][1])
print(ans)