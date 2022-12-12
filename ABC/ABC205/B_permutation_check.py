n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = []
for i in range(1, n+1):
  ans.append(i)

if a == ans:
  print('Yes')
else:
  print('No')