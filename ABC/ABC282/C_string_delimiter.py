n = int(input())
s = input()
cnt = 0
ans = []
for i in range(n):
  if s[i] == '"':
    cnt += 1
    ans.append('"')
  elif s[i] == ',' and cnt%2 == 0:
    ans.append('.')
  elif s[i] == ',' and cnt%2 == 1:
    ans.append(',')
  else:
    ans.append(s[i])

print(*ans, sep='')