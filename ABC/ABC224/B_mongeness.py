def judge():
  for row2 in range(h):
    for row1 in range(row2):
      for col2 in range(w):
        for col1 in range(col2):
          if a[row1][col1] + a[row2][col2] > a[row2][col1] + a[row1][col2]:
            return False
  return True

h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]

print('Yes' if judge() else 'No')