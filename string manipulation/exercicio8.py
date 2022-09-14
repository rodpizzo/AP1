string = str(input("digite algo: "))

a = string.count("a")
e = string.count("e")
i = string.count("i")
o = string.count("o")
u = string.count("u")
espaco = string.count(" ")

total = a+e+i+o+u

print(f"você digitou um total de {total} vogais e {espaco} espaços ")
