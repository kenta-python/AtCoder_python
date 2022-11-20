def is_in_24_hours(h, m):
  return 0 <= h <= 23 and 0 <= m <= 59

def misjudged(h, m):
  a, b = h//10, h%10
  c, d = m//10, m%10
  ac = a*10 + c
  bd = b*10 + d
  return is_in_24_hours(ac, bd)

h, m = map(int, input().split())
while not misjudged(h, m):
  m += 1
  if m == 60:
    m = 0
    h += 1
  if h == 24:
    h = 0

print(h, m)