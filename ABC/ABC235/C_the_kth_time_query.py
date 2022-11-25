from collections import defaultdict

n, q = map(int, input().split())
a = list(map(int, input().split()))
d = defaultdict(list)
for i, x in enumerate(a, 1):
  d[x].append(i)

for _ in range(q):
  x, k = map(int, input().split())
  if k <= len(d[x]):
    print(d[x][k-1])
  else:
    print(-1)

  
