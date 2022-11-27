def solve():
  for i in range(a, b+1):
    if i % c == 0:
      return i
  return -1

a, b, c = map(int, input().split())
print(solve())
