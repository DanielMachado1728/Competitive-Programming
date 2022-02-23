vezes = int(input())
for vez in range(vezes):
    total, pulo = map(int,input().split())
    resposta = 0
    for i in range(1, total+1):
        resposta = (resposta+pulo) % i
    print('Case %d: %d'%(vez+1,resposta+1))
