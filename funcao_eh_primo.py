def eh_primo(num):
    divisores = 0
    if(num == 1 or num == 0):
        return False
    for i in range(2,num):
        if (num == 2):
            break
        if((num % i) == 0):
            divisores += 1
            if(divisores > 1):
                break
    if divisores == 0:
        return True
    else:
        return False

num = int(input())

if eh_primo(num):
    print("S")
else:
    print("N")