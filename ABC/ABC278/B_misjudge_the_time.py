h, m = map(int, input().split())

time = []
for i in range(24):
  for j in range(60):
    time.append([i, j])

num = time.index([h, m])
ans = []
for i in range(num, len(time)):
  if ((time[i][0]//10)*10)+(time[i][1]//10) < 24  and ((time[i][0]%10)*10)+(time[i][1]%10) < 60:
    ans.append(i)
if len(ans) == 0:
  print(0, 0)
else:
  print(*time[ans[0]])
