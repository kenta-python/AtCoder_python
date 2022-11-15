n = int(input())
a = list(map(int, input().split()))

a_even = [i for i in a if i % 2 == 0]
a_odd = [i for i in a if i % 2 == 1]

a_even.sort(reverse=True)
a_odd.sort(reverse=True)

ans=[]
if len(a_even) > 1:
  ans.append(a_even[0]+a_even[1])

if len(a_odd) > 1:
  ans.append(a_odd[0]+a_odd[1])

if len(ans) == 0:
  print(-1)
else:
  print(max(ans))