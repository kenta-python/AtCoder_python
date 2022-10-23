h, w = map(int, input().split())
ans = [0 for i in range(w)]

for i in range(h):
  c = list(input())
  for j in range(w):
    if c[j] == '#':
      ans[j] += 1

print(*ans)
