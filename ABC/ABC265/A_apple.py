X, Y, N = map(int, input().split())

if Y < X*3:
  print((N//3)*Y + (N%3)*X)
else:
  print(N*X)