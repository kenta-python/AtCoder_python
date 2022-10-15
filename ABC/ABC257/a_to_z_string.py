n, x = map(int, input().split())

list = []
for i in range(ord('A'), ord('Z') + 1):
  for j in range(n):
    list.append(chr(i))

print(list[x - 1])

