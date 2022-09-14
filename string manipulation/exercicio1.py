string = str(input("digite uma algo: "))
letra = str(input("digite uma letra: "))

b = string.find(letra)
fim = b+1
fatia = string[:b]+string[fim:]


print(fatia)
