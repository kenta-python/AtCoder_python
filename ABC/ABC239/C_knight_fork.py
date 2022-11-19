x1, y1, x2, y2 = map(int, input().split())

m1 =round((x1+x2)/2)
m2 =round((y1+y2)/2)

ans = []
for i in range(m1-3, m1+4):
  for j in range(m2-3, m2+4):
    if (x1-i)**2 + (y1-j)**2 == 5 and (x2-i)**2 + (y2-j)**2 == 5:
      ans.append([i, j])

if len(ans) == 0:
  print('No')
else:
  print('Yes')