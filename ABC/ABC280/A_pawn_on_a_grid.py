h, w = map(int, input().split())
a = [input().split() for _ in range(h)]

cnt = 0
for i in range(h):
  for j in range(w):
    if a[i][0][j] == '#':
      cnt += 1

print(cnt)


