irv = int(input())
for d in range(2,irv,2):
  quadrado = d ** 2
  print("%d^2 = %d"%(d,quadrado))
if irv % 2 == 0:
  print("%d^2 = %d"%(irv,irv**2))
