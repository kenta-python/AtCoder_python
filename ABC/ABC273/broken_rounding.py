x, k = map(int, input().split())

if x == 1:
  x = 0
else:
  for i in range(k):
    i += 1
    if x%(10**i) >= 5*(10**(i-1)):
      x = (((x//10**i)+1)*(10**i))
    else:
      x = ((x//10**i)*(10**i))

print(x)
