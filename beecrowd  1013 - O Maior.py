a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
if (a-b) < 0:
  absoluto = (a-b)*(-1)
else:
  absoluto = (a-b)
maior = ((a+b)+absoluto)/2
if maior < c:
  print('%d eh o maior'%c)
else:
  print('%d eh o maior'%maior)
