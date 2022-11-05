h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

at = list(zip(*a))

for r in at:
  print(*r)

  
