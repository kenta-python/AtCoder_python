import numpy as np
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
t = [list(input()) for _ in range(h)]

s_t = np.array(s).T.tolist()
t_t = np.array(t).T.tolist()
s_t.sort()
t_t.sort()
if s_t == t_t:
  print('Yes')
else:
  print('No')
