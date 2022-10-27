def solve():
  a, b, k = map(int, input().split())
  
  curr = a 
  ans = 0
  while not (curr >= b):
    ans += 1
    curr *= k
  return ans

print(solve())