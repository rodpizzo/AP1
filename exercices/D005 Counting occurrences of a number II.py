tamanho=int(input(""))
lista=[]
lista = list(map(int, input ().split()))
num=int(input(""))
i=0
a=0
while i<len(lista):
    if lista[i]==num:
        a=a+1
    i+=1

print(a)
    
