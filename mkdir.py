# rangeの中の数字は適宜変えてください

import os

for i in range(227):
  number =str(i + 42).zfill(3)
  os.mkdir('ABC' +str(number))
