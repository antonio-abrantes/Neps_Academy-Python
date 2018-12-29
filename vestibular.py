qtd_questos = int(input())

gabarito = input()

q_marcadas = input()
acertos = 0

#print(list(zip(gabarito, q_marcadas)))
# for g, m in zip(gabarito, q_marcadas):
#     print(g,m)

for i in range(qtd_questos):
    if(gabarito[i] == q_marcadas[i]):
        acertos += 1

print(acertos)