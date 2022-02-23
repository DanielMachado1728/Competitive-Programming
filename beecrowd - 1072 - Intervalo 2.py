a = int(input())
dentro = []
fora = []
for d in range(a):
  x = int(input())
  if 10 <= x <= 20:
    dentro.append(x)
  else:
    fora.append(x)
  tamanho1 = len(dentro)
  tamanho2 = len(fora)
print('{} in'.format(tamanho1))
print('%d out'%tamanho2
