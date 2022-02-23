lista = []
x = int(input())
y = int(input())
if x < y:
  for d in range(x+1,y):
    if d % 2 != 0:
      lista.append(d)
  print(lista)
  tamanho = 0
  for i in (lista):
    tamanho += i
  print(tamanho)
elif x > y:
  for d in range(y+1,x):
    if d % 2 != 0:
      lista.append(d)
  tamanho = 0
  for i in (lista):
    tamanho += i
  print(tamanho)
else:
  print(0)
