n = int(input())
a = list(map(int, input().split()))

batter = []
p = 0
for i in range(n):
  batter.append(0)
  batter = map(lambda sum: sum + a[i], batter)
  batter = list(batter)
  if 4 in batter or 5 in batter or 6 in batter:
    cnt = sum(i >= 4 for i in batter)
    batter.sort()
    del batter[-(cnt):]
    p += cnt

print(p)
