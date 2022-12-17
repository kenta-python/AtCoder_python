n, m = map(int, input().split())
S = []
for _ in range(n):
  s = input()
  S.append(s)

ans = n**2
for i in range(n):
  for j in range(n):
    for k in range(m):
      if S[i][k] == 'x' and S[j][k] == 'x':
        ans -= 1
        break
      elif i == j:
        ans -= 1
        break

print(int(ans/2))




      
  

