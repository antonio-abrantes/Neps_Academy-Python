lista = []

lista.append(int(input()))
lista.append(int(input()))
lista.append(int(input()))

podium = [0,0,0]

for i in range(3):
    posi = 0
    for j in range(3):
        if(lista[i] > lista[j]):
            posi += 1
    podium[posi] = i+1

for m in podium:
    print(m)