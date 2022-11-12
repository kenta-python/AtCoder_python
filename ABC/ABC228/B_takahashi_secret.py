n, x = map(int, input().split())
a = [-1] + list(map(int, input().split()))
flag = [False] * (n+1)
flag[x] = True

now = x
while not flag[a[now]]:
  now = a[now]
  flag[now] = True

print(flag.count(True))



