n = int(input())


def recur(n):
  if n < 2:
    return n
  return n * recur(n - 1)


if n == 0:
  print(1)
else:
  print(recur(n))