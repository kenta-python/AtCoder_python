s = list(input())

a = []
if 'a' not in s:
  print(-1)
else:
  for i in range(len(s)):
    if s[i] == 'a':
      a.append(i)

  print(max(a)+1)


