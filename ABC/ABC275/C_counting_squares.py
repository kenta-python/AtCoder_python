table = []
for i in range(9):
  s = list(input())
  table.append(s)
ans = 0
for i in range(9):
  for j in range(9):
    if table[i][j] == '#':
      for s in range(9-j):
        if table[i][j+s] == '#' and table[i+s][j] == '#' and table[i+s][j+s] == '#':
          ans += 1

# for i in range(9):
#   for j in range(9):     
#     if table[i][j] == '#':
#       for j in range(1, 9-i):
#         if table[i+j][j] == '#' and table[i+int((j/2))][j-int((j/2))] == '#' and table[i+int((j/2))][j+int((j/2))] == '#':
#           ans += 1

print(ans)
      
