n = int(input())
a = list(map(int, input().split()))

nuts = []
for i in a:
  if i > 10:
    nuts.append(i-10)
  else:
    nuts.append(0)

print(sum(nuts))