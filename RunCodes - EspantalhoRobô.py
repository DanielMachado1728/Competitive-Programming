numero_estacoes, numero_comandos, estacao_proxima = map(int,input().split())
comandos = input().split()
#para transformar os elementos  da lista "comandos" em inteiros
for i in range(len(comandos)):
  if comandos[i] == '-1':
    comandos[i] = -1
  else:
    comandos[i] = 1

contagem = 1 #começa na estação 1
vezes_estacao_proxima = 0
for i in comandos:
  if numero_estacoes == estacao_proxima:
    contagem2 = (contagem+1)%(numero_estacoes*2)
    if contagem2 == estacao_proxima:
      contagem += 1
    
  if i == 1:
    contagem = (contagem+1)%numero_estacoes
  if i == -1:
    contagem = (contagem-1)%numero_estacoes

  if contagem == estacao_proxima:
    vezes_estacao_proxima += 1

if estacao_proxima == 1:
  vezes_estacao_proxima += 1
print(vezes_estacao_proxima)
