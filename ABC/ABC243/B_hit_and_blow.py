n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


hit = 0
blow = 0
for i in range(n):
  if a[i] == b[i]:
    hit += 1
  elif a[i] in b:
    blow += 1

print(hit)
print(blow)
  
  