n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

ans = list(map(list, set(map(tuple, a))))
print(len(ans))