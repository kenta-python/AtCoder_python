a, b, c, d, e, f = map(int, input().split())
 
s = (a*b*c) - (d*e*f)
 
print(s%998244353)