a = int(input())
m = int(input())

if(a < 1) or (m < 1):
    print("N")
elif(a + m) > 50:
    print("N")
else:
    print("S")
