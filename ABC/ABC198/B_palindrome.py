n = input()

for i in range(10):
  N = '0'*i + n
  if N == N[::-1]:
    print('Yes')
    exit()
print('No')

