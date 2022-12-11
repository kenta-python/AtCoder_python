n, t = map(int, input().split())
a = list(map(int, input().split()))

sum_a = sum(a)

x = t%sum_a

for i in range(n):
  if a[i] > x:
    print(i+1, x)
    break
  else:
    x = x-a[i]
    
    





