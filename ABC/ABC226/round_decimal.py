a, b = map(int, input().split('.'))

ans = a
if b >= 500:
  ans += 1
print(ans)