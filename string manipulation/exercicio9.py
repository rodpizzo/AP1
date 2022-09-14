palavra1 = str(input("digite uma palavra: "))
palavra2 = str(input("digite uma palavra: "))

palavra1_ordenada = sorted(palavra1)
palavra2_ordenada = sorted(palavra2)

if palavra1_ordenada == palavra2_ordenada:
    print("é um anagrama")
else:
    print("não é um anagrama")
