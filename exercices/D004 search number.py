tamanho=int(input(""))
lista=[]
lista = list(map(int, input ().split()))
num=int(input(""))
i=0
a=0
while i<len(lista):
    if lista[i]==num:
        a=i
    i+=1
if num not in lista:
    a=-1
print(a)
    
