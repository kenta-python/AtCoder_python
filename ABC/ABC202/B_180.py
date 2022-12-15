s = input()
t = s[::-1]
ans = []
for i in range(len(s)):
  if t[i] == '0':
    ans.append(0)
  elif t[i] == '1':
    ans.append(1)
  elif t[i] == '6':
    ans.append(9)
  elif t[i] == '8':
    ans.append(8)
  else:
    ans.append(6)

print(*ans, sep='')