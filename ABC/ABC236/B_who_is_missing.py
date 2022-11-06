n = int(input())
a = list(map(int, input().split()))

cnt = [0]*(n+1)

for i in range(4*n-1):
  cnt[a[i]] += 1

for j in range(n+1):
  if cnt[j] == 3:
    print(j)