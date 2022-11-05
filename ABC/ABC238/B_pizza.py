n = int(input())
a = list(map(int, input().split()))
b = [0, 360]

cur = 0
for i in a:
  cur += i
  d = cur%360
  b.append(d)

b.sort()

c = [b[i+1] - b[i] for i in range(len(b) - 1)]
print(max(c))