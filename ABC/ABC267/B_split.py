s = "?"+input()

if s[1] == '1':
  print('No')
  exit()

x = ''
if s[7] == '1':
  x += 'A'
else:
  x += 'B'

if s[4] == '1':
  x += 'A'
else:
  x += 'B'

if s[2] == '1' or s[8] == '1':
  x += 'A'
else:
  x += 'B'

if s[5] == '1':
  x += 'A'
else:
  x += 'B'

if s[3] == '1' or s[9] == '1':
  x += 'A'
else:
  x += 'B'

if s[6] == '1':
  x += 'A'
else:
  x += 'B'

if s[10] == '1':
  x += 'A'
else:
  x += 'B'

if 'ABA' in x:
  print('Yes')
elif 'ABBA' in x:
  print('Yes')
elif 'ABBBA' in x:
  print('Yes')
elif 'ABBBBA' in x:
  print('Yes')
elif 'ABBBBBA' in x:
  print('Yes')
else:
  print('No')