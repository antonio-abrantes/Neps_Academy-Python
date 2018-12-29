import math

qtd = int(input())

lista = input().split()

for num in lista:
    print("{:.4f}".format(math.sqrt(float(num))))