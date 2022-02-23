n = int(input())
for d in range(n):
  x = int(input())
  if x == 0:
    impressao = 'NULL'
  if x > 0:
    if x % 2 == 0:
      impressao  = 'EVEN POSITIVE'
  if x < 0:
    if x % 2 == 0:
      impressao = 'EVEN NEGATIVE'
  if x > 0:
    if x % 2 != 0:
      impressao = 'ODD POSITIVE'
  if x < 0:
    if x % 2 != 0:
      impressao = 'ODD NEGATIVE'
  print(impressao)
