prince,kaillena = map(int,input().split())
if prince % kaillena == 0 or kaillena % prince == 0:
  print('Sao Multiplos')
else:
  print('Nao sao Multiplos')
