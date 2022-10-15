N = list(map(int, input().split()))

N.sort()
if (N[0] == N[1] and N[2] == N[4]) or (N[0] == N[2] and N[3] == N[4]):
  print('Yes')
else:
  print('No')
