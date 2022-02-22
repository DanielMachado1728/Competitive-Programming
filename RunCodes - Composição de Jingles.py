notas = {'w':1,'h':1/2,'q':1/4,'e':1/8,'s':1/16,'t':1/32,'x':1/64}
while True:
  musica = input().lower().replace('\n','').replace('\r','')
  if musica == '*':
    break
  l = []
  soma = 0
  for i in musica:
    if i == '/':
      l.append(soma)
      soma = 0
    for chave in notas:
      if i == chave:
        soma += notas[chave]
  #print(l)
  soma2 = 0
  for compasso in l:
    if compasso == 1:
      soma2 += compasso
   
  print(int(soma2))
