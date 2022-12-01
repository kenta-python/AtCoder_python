n = int(input())

name = []
Flag = False
for _ in range(n):
  s = input()
  if s in name:
    Flag = True
  else:
    name.append(s)
  
print('Yes' if Flag else 'No')
  
