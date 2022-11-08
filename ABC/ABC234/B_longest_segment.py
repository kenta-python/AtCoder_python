def solve():
  ans = 0
  for i in range(n):
    x1, y1 = xy[i]
    for j in range(i):
        x2, y2 = xy[j]
        l = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        ans = max(ans, l)
  return ans

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
print(solve())
