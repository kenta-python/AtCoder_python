N = int(input())

a, b = N//16, N%16
X = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

if a >= 10:
  a = X[a]
if b >= 10:
  b = X[b]

print(str(a)+str(b))

'''
別解
print("{:02X}".format(int(input())))

参考
https://note.nkmk.me/python-format-zero-hex/
'''
