palavra = str(input("digite sua palavra: "))
i=0
b=-1
a=0

while i<len(palavra):
    if palavra[i] == palavra[b]:
        i = i + 1
        b = b - 1
        a = a + 1
    else:
        print("não é um palindromo")
        i=len(palavra)
if a == len(palavra):
    print("é um palindromo")
