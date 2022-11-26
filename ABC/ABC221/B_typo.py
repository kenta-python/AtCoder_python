s = list(input())
t = list(input())
a = sorted(s)
b = sorted(t)
diff = []

for i in range(len(s)):
  if s[i] == t[i]:
    diff.append('0')
  else:
    diff.append('1')

x = ''.join(diff)
if ('11' in x and diff.count('1') == 2 and a == b) or s == t:
  print('Yes')
else:
  print('No')