n = input()
l = input().split()

a = 0
b = 0

for acao in l:
    if(acao == '1'):
        if a == 1:
            a = 0
        else:
            a = 1
    elif(acao == '2'):
        if a == 1:
            a = 0
        else:
            a = 1

        if b == 1:
            b = 0;
        else:
            b = 1

print(a)
print(b)