n = int(input())
node = [0]*n

for i in range(n-1):
  a, b = map(int, input().split())
  node[a-1] += 1
  node[b-1] += 1

if n-1 in node:
  print('Yes')
else:
  print('No')
  