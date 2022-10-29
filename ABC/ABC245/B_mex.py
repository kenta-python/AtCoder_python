n = int(input())
a = set(map(int, input().split()))
t = {i for i in range(2010)}
d = t-a
print(min(d))
  