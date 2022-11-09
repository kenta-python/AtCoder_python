N = int(input())
S = {}

for _ in range(N):
  s = input()
  if s in S:
    S[s] += 1
  else:
    S[s] = 1

ans = max(S, key=S.get)
print(ans)
  