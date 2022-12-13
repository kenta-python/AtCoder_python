def main():
  x, y = map(int, input().split())
  if x == y:
    print(x)
  else:
    a = [True] * 3
    a[x] = False
    a[y] = False
    print(a.index(True))

if __name__ == '__main__':
  main()
