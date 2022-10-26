s = input()
set_s = set(s)
lower_s = s.lower()
upper_s = s.upper()
if len(set_s) == len(s) and s != lower_s and s != upper_s:
  print('Yes')
else:
  print('No')