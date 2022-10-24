def solve():
  n, w = map(int, input().split())
  a = list(map(int, input().split())) + [0, 0]
  good = [False]*(w+1)

  for i in range(n+2):
    for j in range(i):
      for k in range(j):
        W = a[i] + a[j] +a[k]
        if W <= w:
          good[W] = True
  return good.count(True)

print(solve())