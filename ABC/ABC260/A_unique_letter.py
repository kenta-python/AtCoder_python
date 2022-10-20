S = input()
s = set(S)

if len(s) == 3:
  print(S[0])
elif len(s) == 1:
  print(-1)
else:
  for i in range(3):
    if S.count(S[i]) == 1:
      print(S[i])