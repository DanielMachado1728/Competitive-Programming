while True:
  a,b = map(int,input().split())
  if a < 1 or b < 1:
    break
  else:
    if a > b:
      soma  = 0
      for d in range(b,a+1):
        soma += d
        print(d,end=' ')
      print('Sum=%d'%soma)
    elif a < b:
      soma = 0
      for i in range(a,b+1):
        soma += i
        print(i,end=' ')
      print('Sum=%d'%(soma))
        
