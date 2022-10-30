# メモ化再帰

n = int(input())
from functools import lru_cache

@lru_cache(maxsize=1000)
def f(n):
  if n == 0:
    return 1
  else:
    return f(n//2) + f(n//3)

print(f(n))