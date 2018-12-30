senha = 2018
tentativa = 0

cont = 0
while(senha != tentativa):
    tentativa = int(input())
    if(tentativa != senha):
        cont += 1

print(cont)