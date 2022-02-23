a = 0
l = []
while a < 6:
  x = float(input())
  a += 1
  if x > 0:
    l.append(x)
  else:
    continue
  tamanho = len(l)
print('{} valores positivos'.format(tamanho))


  
