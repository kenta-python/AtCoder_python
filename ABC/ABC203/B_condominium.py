n, k = map(int, input().split())
room = []
for i in range(1, n+1):
  for j in range(1, k+1):
    room.append((i*100) + j)

print(sum(room))