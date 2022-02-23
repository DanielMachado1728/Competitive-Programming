v = int(input())
if v % 2 == 0:
  for irv in range(v+1,v+12,2):
    print(irv)
else:
  for irv in range(v,v+11,2):
    print(irv)
