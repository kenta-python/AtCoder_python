from collections import defaultdict
n = int(input())
S = defaultdict(int)

for i in range(n):
  s = input()
  if S[s] == 0:
    print(s)
  else:
    x = S[s]
    print(f'{s}({x})')
  S[s] += 1