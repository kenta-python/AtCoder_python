n, x = map(int, input().split())
a = list(map(int, input().split()))
a_sale = []
for i in range(len(a)):
  if i%2 == 0:
    a_sale.append(a[i])
  else:
    a_sale.append(a[i]-1)

sum_a = sum(a_sale)

if sum_a <= x:
  print('Yes')
else:
  print('No')