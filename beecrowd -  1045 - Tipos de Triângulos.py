a,b,c = map(float,input().split())
l = []
l.append(a)
l.append(b)
l.append(c)
ordem = sorted(l,key=int, reverse=True)
a = ordem[0]
b = ordem[1]
c = ordem[2]
if a >= b+c:
  print("NAO FORMA TRIANGULO")
else:
  if (a**2) == (b**2) + (c**2):
    print('TRIANGULO RETANGULO')
  if (a**2) > (b**2) + (c**2):
    print('TRIANGULO OBTUSANGULO')
  if (a**2) < (b**2) + (c**2):
    print('TRIANGULO ACUTANGULO')
  if a == b and b == c:
    print('TRIANGULO EQUILATERO')
  elif a == b:
    print('TRIANGULO ISOSCELES')
  elif a == c:
    print('TRIANGULO ISOSCELES')
  elif b == c:
    print('TRIANGULO ISOSCELES')
