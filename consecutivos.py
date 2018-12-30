qtd = int(input())

numeros = input().split()
sequencias = []

for i in range(qtd):
    cont = 0
    for j in range(i, qtd):
        print(i)
        if(int(numeros[i]) == int(numeros[j])):
            cont += 1
        else:
            break

    sequencias.append(cont)
    i += cont

sequencias = sorted(sequencias)
print(sequencias)

print(sequencias[len(sequencias)-1])