lista1=[]
lista2=[]
i=0
a=0
soma=0
media=0
b=0
x=0
y=0

##while i<7:
##    temp=int(input(""))
##    lista1.append(temp)
##    i+=1
lista1=list(map(int,input().split()))
while a<7:
    soma=soma+lista1[a]
    a+=1
    
media=soma/7
x=0
while b<len(lista1):
    x=lista1[b]
    b+=1
    if x>media:
        lista2.append(x)
y=len(lista2)
print(y)

        

    
