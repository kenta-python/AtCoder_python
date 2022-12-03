s = input()
t = input()
ans = 1
for i in range(len(t)-1):
  if s[i] == t[i]:
    ans += 1
    if i == len(s)-1:
      print(ans)
      break
  else:
    print(ans)
    break

