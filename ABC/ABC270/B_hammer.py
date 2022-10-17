x, y, z = map(int, input().split())

if y > 0 and x < y:
  print(abs(x)); exit()
elif y < 0 and y < x:
  print(abs(x)); exit()

if 0 < y < z or z < y < 0:
  print(-1); exit()
else:
  ans = abs(z)
  ans += abs(y-z)
  ans += abs(x-y)
  print(ans); exit()

print(-1)