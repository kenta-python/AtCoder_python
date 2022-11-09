s = list(input())
t = list(input())
 
ascii_s = list(map(lambda x: ord(x), s))
ascii_t = list(map(lambda x: ord(x), t))
 
C = {(x - y) % 26 for x, y in zip(ascii_s, ascii_t)}

if len(C) == 1:
  print('Yes')
else:
  print('No')






