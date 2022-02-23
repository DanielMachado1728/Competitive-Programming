ciclo = 0
l = []
while ciclo < 6:
  a = float(input())
  ciclo = ciclo + 1
  if a > 0:
    l.append(a)
  tamanho = len(l)
  media = (sum(l))/tamanho
print('%d valores positivos'%tamanho)
print('%.1f'%media)
