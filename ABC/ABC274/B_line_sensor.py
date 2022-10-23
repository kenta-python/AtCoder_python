h, w = map(int, input().split())
c = [input().split() for _ in range(h)]

ans = []
for i in range(w):
  cnt = 0
  for j in range(h):
    a = list(c[j][0])
    if a[i] == '#':
      cnt += 1
  ans.append(cnt)

ans_str = [str(a) for a in ans]
print(" ".join(ans_str))
# TLE
