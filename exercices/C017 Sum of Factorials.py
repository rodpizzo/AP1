tamanho=int(input(""))
a=1
soma=0
while a<=tamanho:
    num=a
    i=1
    fat=1
    
    while i<=num:
        fat=fat*(i)
        i=i+1
    a+=1
    soma=soma+fat
    
print(soma+1)
