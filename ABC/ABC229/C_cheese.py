n, w = map(int, input().split())
ch = [list(map(int, input().split())) for _ in range(n)]

ch.sort(reverse=True)

ans = 0
for j in range(len(ch)):
  if w >= ch[j][1]:
    ans += ch[j][0]*ch[j][1]
    w -= ch[j][1]
  else:
    ans += ch[j][0]*w
    break

print(ans)




