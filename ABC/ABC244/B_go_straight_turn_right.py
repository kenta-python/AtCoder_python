n = int(input())
t = input()

x, y = 0,0
d = 1
for i in range(n):
  if t[i] == 'S':
    if d%4 == 1:
      x += 1
    elif d%4 == 2:
      y -= 1
    elif d%4 == 3:
      x -= 1
    else:
      y += 1
  else:
    d += 1

print(x, y)
