x,y,d,e = map(float,input().split())
ponderada = ((2*x) +   (3* y) + (4*d) +  (1*e)) / 10
if ponderada >= 7:
  print('Media: %.1f\nAluno aprovado.'%ponderada)
elif ponderada < 5:
    print('Media: %.1f\nAluno reprovado.'%ponderada)
else:
  print('Media: %.1f\nAluno em exame.'%ponderada)
  nova = float(input())
  if (nova+ponderada/2) >= 5:
    print('Nota do exame: %.1f\nAluno aprovado.\nMedia final: %.1f'%(nova,((nova+ponderada)/2)))
  else:
    print('Nota do exame: %.1f\nAluno reprovado.\nMedia final: %.1f'%(nova,((nova+ponderada)/2)))
