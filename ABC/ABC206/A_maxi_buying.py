n = int(input())

import math
price = 206
ans = math.floor(n*1.08)

if ans > price:
  print(':(')
elif ans == price:
  print('so-so')
else:
  print('Yay!')