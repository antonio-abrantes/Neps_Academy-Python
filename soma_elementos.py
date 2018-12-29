qtd = input()
qtd = int(qtd)

lista = input().split()

soma = 0
for i in range(0, qtd):
    soma = soma + int(lista[i])

print(soma)