s = input()
s_list = []

for i in range(len(s)):
  s_list.append(s[i:] + s[:i])

s_list.sort()
print(s_list[0])
print(s_list[len(s)-1])