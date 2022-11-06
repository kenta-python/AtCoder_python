n, m = map(int, input().split())
a = [[] for _ in range(n)]

for _ in range(m):
  x, y = map(int, input().split())
  a[x-1].append(y)
  a[y-1].append(x)

for i , j in enumerate(a):
  j.sort()
  print(len(j), *j)