n = int(input())
sum = 0
ans = 0
money = 1

while sum < n:
  sum += money
  money += 1
  ans += 1

print(ans)
