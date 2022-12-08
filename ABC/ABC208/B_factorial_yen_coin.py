import math
p = int(input())

ans = 0

for i in range(10, 0, -1):
  coin = math.factorial(i)
  while coin <= p:
    p -= coin
    ans += 1

print(ans)