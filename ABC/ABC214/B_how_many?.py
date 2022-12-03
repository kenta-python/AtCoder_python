s, t = map(int, input().split())

ans = 0
for a in range(0, s+1):
  for b in range(0, s+1):
    for c in range(0, s+1):
      x = a+b+c
      y = a*b*c
      if x <= s and y <= t:
        ans += 1

print(ans)

