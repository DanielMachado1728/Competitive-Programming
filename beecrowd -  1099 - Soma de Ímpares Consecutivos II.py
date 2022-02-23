casos = int(input())
for d in range(casos):
  x,y = map(int,input().split())
  if x <= y:
     l=[d for d in range(x+1,y) if d % 2 == 1]
     print(sum(l))
  else:
    l = [d for d in range(y+1,x) if d % 2 == 1]
    print(sum(l))
