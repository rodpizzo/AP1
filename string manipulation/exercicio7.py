palavra = str(input("digite sua palavra: "))
palavra_nova = ''
tamanho = len(palavra)
i=-1

while i>=(-tamanho):
    palavra_nova = palavra_nova + palavra[i]
    i = i-1
palavra_nova = palavra_nova.upper()
print (palavra_nova)
    

    
