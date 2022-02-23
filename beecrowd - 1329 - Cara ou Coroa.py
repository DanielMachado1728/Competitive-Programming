while True:
    vez = int(input())
    if vez == 0:
        break
    p = input().split(' ')
    maria = 0
    joao = 0
    for l in range(vez):
        if int(p[l]) == 0:
            maria += 1
        else:
            joao += 1
    print("Mary won "+str(maria)+" times and John won "+str(joao)+" times")
