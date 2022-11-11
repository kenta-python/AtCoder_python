def judge():
  a, b = input().split()
  x, y = a.zfill(20), b.zfill(20)

  for i, j in zip(x, y):
    if int(i) + int(j) >= 10:
      return 'Hard'
  return 'Easy'

print(judge())
  



