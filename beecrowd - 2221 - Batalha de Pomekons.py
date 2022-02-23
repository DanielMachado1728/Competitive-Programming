n = int(input())
for i in range(n):
  bonus = int(input())
  bonus2 = bonus
  valor_golpe = input().split()
  if int(valor_golpe[2]) % 2 != 0:
    bonus = 0
  valor_golpe2 = input().split()
  if int(valor_golpe2[2]) % 2 != 0:
    bonus2 = 0
  dabriel = (int(valor_golpe[0])+int(valor_golpe[1]))/2+bonus
  guarte = (int(valor_golpe2[0])+int(valor_golpe2[1]))/2+bonus2
  if dabriel == guarte:
    print('Empate')
    continue
  if dabriel > guarte:
    print('Dabriel')
  else:
    print('Guarte')
