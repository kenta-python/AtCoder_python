n = int(input())
s = input()

for i in range(n):
  if s[i] == '1':
    index = i
    break

if index%2 == 0:
  print('Takahashi')
else:
  print('Aoki')
