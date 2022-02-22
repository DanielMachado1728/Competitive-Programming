d = {}
casos = int(input())
for i in range(casos):
  produtos_disponiveis = int(input())
  for j in range(produtos_disponiveis):
    fruta,preco = input().split()
    preco = float(preco)
    d['%s'%fruta] = preco
  deseja_comprar = int(input())
  soma = 0
  for i in range(deseja_comprar):
    fruta_levar,qtd_levar = input().split()
    qtd_levar = int(qtd_levar)
    for k,v in d.items():
      if fruta_levar == k:
        soma += v*qtd_levar
  print('R$ %.2f'%(soma))
