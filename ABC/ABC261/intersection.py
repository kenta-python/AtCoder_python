l1, r1, l2, r2 = map(int, input().split())

lmax = max(l1, l2)
rmin = min(r1, r2)

if rmin - lmax < 0:
  print(0)
else:
  print(rmin-lmax)