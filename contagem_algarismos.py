num = int(input())

lista = []

for i in range(num):
    lista.append(input())

ocorrencia = []
for i in range(10):
    cont = 0
    for str in lista:
        for j in range(len(str)):
            if (i == int(str[j])):
                cont += 1
    ocorrencia.append(cont)

for i in range(10):
    print("{} - {}".format(i, ocorrencia[i]))