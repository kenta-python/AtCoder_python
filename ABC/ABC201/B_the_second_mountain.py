n = int(input())
mountain = []
for i in range(n):
  s, t = map(str, input().split())
  t = int(t)
  mountain.append([t, s])
mountain.sort(reverse=True)
print(mountain[1][1])