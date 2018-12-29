a, b, c = input().split()

ganhador = None

if a != b and a != c:
    ganhador = "A"
elif b != a and b != c:
    ganhador = "B"
elif c != a and c != b:
    ganhador = "C"
else:
    ganhador = "*"

print(ganhador)