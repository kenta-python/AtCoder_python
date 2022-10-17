s = input()
t = input()

prefix = t[:len(s)]

if prefix == s:
  print('Yes')
else:
  print('No')