n, m = map(int, input().split())
p = set()

for i in range(m):
  x = list(map(int, input().split()[1:]))
  for j in range(len(x)):
    for k in range(j + 1, len(x)):
      p.add((x[j], x[k]))

if n*(n-1) // 2 == len(p):
   print('Yes')
else:
   print('No')