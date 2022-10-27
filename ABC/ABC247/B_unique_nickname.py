def judge():
  def judge2(u, idx):
    for i in range(n):
      if i == idx: continue
      if u in ST[i]:
        return False
    return True
  
  n = int(input())
  ST = [input().split() for _ in range(n)]
  for i in range(n):
    si, ti = ST[i]
    if not (judge2(si , i) or judge2(ti, i)):
      return False
  return True

print('Yes' if judge() else 'No')