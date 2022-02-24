casos = int(input())
for i in range(casos):
  valores = input().split()
  media_ponderada = ((float(valores[0])*2) + float(valores[1])*3 + float(valores[2])*5)/10
  print('%.1f'%media_ponderada)
