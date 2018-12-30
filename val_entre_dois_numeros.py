num1 = int(input())
num2 = int(input())

if(num2 < 0):
    temp = num2
    num2 = num1
    num1 = temp

num2 += 1

for i in range(num1, num2):
    if(i < (num2-1)):
        print(i, end=" ")
    else:
        print(i, end="")