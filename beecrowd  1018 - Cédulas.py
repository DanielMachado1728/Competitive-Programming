n = int(input())
d100 = n //100
resto = n%100
d50 = resto // 50
resto = resto%50
d20 = resto // 20
resto = resto % 20
d10 = resto // 10
resto = resto % 10
d5 = resto // 5
resto = resto % 5
d2 = resto // 2
resto = resto % 2
d1 = resto // 1
resto = resto % 1

print('%d\n%d nota(s) de R$ 100,00\n%d nota(s) de R$ 50,00\n%d nota(s) de R$ 20,00\n%d nota(s) de R$ 10,00\n%d nota(s) de R$ 5,00\n%d nota(s) de R$ 2,00\n%d nota(s) de R$ 1,00'%(n,d100,d50,d20,d10,d5,d2,d1))
