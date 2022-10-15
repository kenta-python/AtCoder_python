k = int(input())

if k < 60:
  k = str(k).zfill(2)
  print("21:" + k)
else:
  k = str(k - 60).zfill(2)
  print("22:" + k)

'''
k = int(input())
if k < 60:
  h = 21
else:
  h = 22
m = k%60
print('{}:{:02}'.format(h, m))
'''
