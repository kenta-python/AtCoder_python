n = int(input())
s = [list(input().split()) for _ in range(n)]

set_s = list(map(list, set(map(tuple, s))))

ans = 0
for i in range(n):
  if s[i][0][0] in ['H', 'D', 'C', 'S']:
    if s[i][0][1] in ['A' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , 'T' , 'J' , 'Q' , 'K']:
      if len(set_s) == len(s):
        ans += 1

print('Yes' if ans == n else 'No')



  


