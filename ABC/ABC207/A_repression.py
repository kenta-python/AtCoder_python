a, b, c = map(int, input().split())

X = [a+b, b+c, c+a]

print(max(X))