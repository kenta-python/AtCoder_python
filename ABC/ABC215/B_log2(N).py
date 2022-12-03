n = int(input())

for i in range(100):
  if n<2**i:
    print(i-1)
    break