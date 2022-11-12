n, k, a = map(int, input().split())

first = n - a + 1
if (k - first)%n == 0:
  print(n)
else:
  print((k - first)%n)