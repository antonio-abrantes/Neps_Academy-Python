a, b = input().split()

a = float(a)
b = float(b)

media = (a + b) / 2

if (media >= 4 and media < 7):
    print("Recuperacao")
elif (media >= 7):
    print("Aprovado")
else:
    print("Reprovado")