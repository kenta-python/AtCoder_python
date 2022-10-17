s = [list(input()) for _ in range(10)]

xmx, xmn, ymx, ymn = 0, 100, 0, 100
for i in range(10):
  for j in range(10):
    if s[i][j] == '#':
      xmx = max(xmx, i)
      xmn = min(xmn, i)
      ymx = max(ymx, j)
      ymn = min(ymn, j)

print(xmn+1, xmx+1)
print(ymn+1, ymx+1)

