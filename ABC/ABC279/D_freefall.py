import math
a, b = map(int, input().split())
cur = a
i = 1
def f(i):
  return (b*i) + (a/math.sqrt(i+1))
# while True:
#   if cur > (b*i) + (a/math.sqrt(i+1)):
#     cur = (b*i) + (a/math.sqrt(i+1))
#     i += 1
#   else:
#     print(cur)
#     break

while True:
  if f(i-1) < f(i):
    print(f(i-1))