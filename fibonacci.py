def fibonacci():
    lista = []
    x = 0
    y = 1
    lista.append(x)
    lista.append(y)

    for i in range(2, 32):
        aux = y
        y = x + aux
        x = aux
        lista.append(y)

    return lista

n = int(input())
lista = fibonacci()

print(lista[n+1])