op = input()

numeros = input().split()

if op == "M":
    result = float((numeros[0])) * float((numeros[1]))
    print("{:.2f}".format(result))
else:
    result = float((numeros[0])) / float((numeros[1]))
    print("{:.2f}".format(result))