n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
max_a = max(a)
min_b = min(b)

ans = min_b - max_a + 1

if min_b - max_a < 0:
  print(0)
else:
  print(ans)
