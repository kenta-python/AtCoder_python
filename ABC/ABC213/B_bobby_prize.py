n = int(input())
a = list(map(int, input().split()))

a_sort = sorted(a, reverse=True)
print(a.index(a_sort[1])+1)