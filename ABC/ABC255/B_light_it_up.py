n, k = map(int, input().split())
a = list(map(int, input().split()))

p = [[0, 0]]

for i in range(n):
  x, y = map(int, input().split())
  p.append([x,y])

dist = [[0]*(n+1) for i in range(k)]

from math import sqrt

def calcdist(a, b):
  return sqrt((p[a][0] - p[b][0])**2 +(p[a][1] - p[b][1])**2)

for gyou in range(k):
  for retsu in range(1, n+1):
    dist[gyou][retsu] = calcdist(a[gyou], retsu)
retsumin=[0]*(n+1)

for retsu in range(1, n+1):
  d = 10**10
  for gyou in range(k):
    d=min(d, dist[gyou][retsu])

  retsumin[retsu] = d

print(max(retsumin))
