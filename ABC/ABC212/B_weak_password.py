def solve():
  if len(set(X)) == 1:
    return 'Weak'
  for i in range(3):
    if (int(X[i])+1) % 10 != int(X[i+1]):
      return 'Strong'
  return 'Weak'

X = input()
print(solve())