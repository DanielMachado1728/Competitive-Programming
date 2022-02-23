a = int(input())
cont = 0
soma = 0
while True:
  b = int(input())
  if b <= a:
    continue
  break

for i in range(a,b):
  soma += i
  cont += 1
  if soma > b:
    break

print(cont)
