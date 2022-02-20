codigo,qtd = map(int,input().split())
if codigo == 1:
  print('Total: R$ %.2f'%(qtd*4))
elif codigo == 2:
  print('Total: R$ %.2f'%(qtd*4.5))
elif codigo == 3:
  print('Total: R$ %.2f'%(qtd*5))
elif codigo == 4:
  print('Total: R$ %.2f'%(qtd*2))
else:
  print('Total: R$ %.2f'%(qtd*1.5))
