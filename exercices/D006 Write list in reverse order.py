tamanho=int(input(""))
lista=[]
lista = list(map(int, input ().split()))
i=(len(lista)-1)
x=tamanho-1

while x>=0:
    print( lista[x], end=" ")
    x=x-1
