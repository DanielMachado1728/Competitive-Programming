salario = float(input())
if 0 < salario<=400:
  reajuste = salario*0.15
  novo_salario = salario + reajuste
  percentual = '15 %'
elif 400.01 <= salario <= 800:
  reajuste = salario*0.12
  novo_salario = salario + reajuste
  percentual = '12 %'
elif 800.01 <= salario <= 1200:
  reajuste = salario*0.10
  novo_salario = salario + reajuste
  percentual = '10 %'
elif 1200.01 <= salario <= 2000:
  reajuste = salario*0.07
  novo_salario = salario + reajuste
  percentual = '7 %'
elif salario > 2000:
  reajuste = salario*0.04
  novo_salario = salario + reajuste
  percentual = '4 %'
print('Novo salario: %.2f'%(novo_salario))
print('Reajuste ganho: %.2f'%(reajuste))
print('Em percentual: %s'%(percentual))
