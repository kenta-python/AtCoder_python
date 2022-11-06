n = int(input())
h = list(map(int, input().split()))

for i in range(n):
  if i == n-1:
    print(h[i])
  else:
    if h[i] >= h[i+1]:
      print(h[i])
      exit()