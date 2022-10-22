n, m, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

for i in range(q):
  if a[(l[i]-1)] < n and (a[(l[i]-1)] + 1) not in a:
    a[(l[i]-1)] += 1
    a.sort()

a_str = [str(j) for j in a]
ans = ' '.join(a_str)
print(ans)