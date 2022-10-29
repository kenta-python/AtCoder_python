n = int(input())
a = list(map(int, input().split()))
 
max = max(a)
ans = a.index(max) + 1
 
print(ans)