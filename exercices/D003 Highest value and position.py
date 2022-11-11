tamanho=int(input(""))
i=0
lista=[]

lista = list(map(int, input ().split()))

i=0
a=0
maior=lista[0]
while i<len(lista):
    if lista[i]>maior:
        maior=lista[i]
        a=i
    i+=1
print(maior)
print(a)
