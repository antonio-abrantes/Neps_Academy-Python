n = int(input())

visualizacaoes = []

for i in range(n):
    a = int(input())
    visualizacaoes.append(a)


soma = 0;
resp = -1
for i, v in enumerate(visualizacaoes):
    dia = i + 1
    soma = soma + v
    if soma >= 1000000 and resp == -1:
        resp = dia

print(resp)