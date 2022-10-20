n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans=[]
mathp=[]

for i in range(n):
  mathp.append([a[i],-(i+1)])

mathp.sort(reverse=True)

for i in range(x):
  ans.append(-mathp[i][1])

engp=[]

for i in range(n):
  if (i+1) not in ans:
    engp.append([b[i], -(i+1)])

engp.sort(reverse=True)

for i in range(y):
  ans.append(-engp[i][1])

allp=[]

for i in range(n):
  if (i+1) not in ans:
    allp.append([a[i]+b[i], -(i+1)])

allp.sort(reverse=True)

for i in range(z):
  ans.append(-allp[i][1])

ans.sort()

for x in ans:
  print(x)