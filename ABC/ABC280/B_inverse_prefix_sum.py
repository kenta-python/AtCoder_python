n = int(input())
s = list(map(int, input().split()))

sum_s = []
for i in range(len(s)):
  if i != 0:
    sum_s.append(s[i]-s[i-1])
  else:
    sum_s.append(s[i])

print(*sum_s)