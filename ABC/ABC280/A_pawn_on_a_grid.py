h, w = map(int, input().split())

cnt = 0
for i in range(h):
  s = list(input())
  for j in range(w):
    if s[j] == '#':
      cnt += 1

print(cnt)