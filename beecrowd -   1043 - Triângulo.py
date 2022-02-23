a,b,c = map(float,input().split())
if ((b-c)<a<b+c) >0:
  if  ((a-c)<b<a+c) >0:
    if ((a-b)<c<a+b)>0:
      print('Perimetro = {:.1f}'.format(a+b+c))
else:
  at = ((a+b)*c)/2
  print("Area = {:.1f}".format(at))
