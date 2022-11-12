n = int(input())
s = list(map(int, input().split()))
flag = [False]*n

for x in range(len(s)):
  for i in range(1,1001):
    for j in range(1,1001):
      if s[x] == (4*i*j)+(3*i)+(3*j):
        flag[x-1] = True

print(flag.count(False))
