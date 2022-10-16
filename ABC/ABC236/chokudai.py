s = input()
a, b = map(int, input().split())

list_s = list(s)

list_s[a-1], list_s[b-1] = list_s[b-1], list_s[a-1]

print("".join(list_s))