def operaco(lista):
    if(lista[1] == "*"):
        return int(lista[0]) * int(lista[2])
    else:
        return int(lista[0]) + int(lista[2])

mem = int(input())
linha = input().split()

resultado = operaco(linha)

if(resultado > mem):
    print("OVERFLOW")
else:
    print("OK")
