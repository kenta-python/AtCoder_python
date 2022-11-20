n, q = map(int, input().split())
d = {}
from collections import defaultdict
d = defaultdict(int)

for i in range(q):
  t, a, b = input().split()
  a = a.zfill(10)
  b = b.zfill(10)
  if t == '1':
    d[a+b] = 1
  elif t == '2':
    d[a+b] = 0
  else:
    if d[a+b] == 1 and d[b+a] == 1:
      print('Yes')
    else:
      print('No')
