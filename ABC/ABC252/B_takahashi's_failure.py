n, k = map(int, input().split())
a = (list(map(int, input().split())))
b = (list(map(int, input().split())))

for i in range(k):
  if a[b[i]-1] == max(a):
    print('Yes')
    exit()

print('No')