s = input()

vogais = ['a', 'e', 'i', 'o', 'u']

r = ''

for c in s:
    if c in vogais:
        r += c

if r == r[::-1]:
    print("S")
else:
    print("N")