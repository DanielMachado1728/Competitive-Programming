a,b,c = map(int,input().split())
if a < b < c:
  print(a)
  print(b)
  print(c)
elif a < c < b:
  print(a)
  print(c)
  print(b)
elif b<a<c:
  print(b)
  print(a)
  print(c)
elif b<c<a:
  print(b)
  print(c)
  print(a)
elif c<a<b:
  print(c)
  print(a)
  print(b)
elif c<b<a:
  print(c)
  print(b)
  print(a)
print()
print(a)
print(b)
print(c)
