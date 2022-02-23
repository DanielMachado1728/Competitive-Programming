ciclo = 0
pares = []
while ciclo < 5:
  entrada = float(input())
  ciclo += 1
  if entrada % 2 == 0:
    pares.append(entrada)
  quantidade = len(pares)
print('{} valores pares'.format(quantidade))
