a, b, c, d = map(int, input().split())

import math

if (c*d)-b <= 0:
  print(-1)
else:
  print(math.ceil(a/((c*d)-b)))