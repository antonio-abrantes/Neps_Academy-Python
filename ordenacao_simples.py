
qtd = int(input())

entrada = input().split()
lista = []

for c in entrada:
    lista.append(int(c))

ordenada = sorted(lista)

for i in range(qtd):
    if(i < qtd-1):
        print(ordenada[i], end=" ")
    else:
        print(ordenada[i], end="")