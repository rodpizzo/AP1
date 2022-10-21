num=int(input(""))
a=1
soma=0
while a<=num:
    count=0
    i=1
    x=0

    while i<=a:
        x=a%i
        y=a%1
        if x==0 and y==0:
            count=count+1
        i+=1
    
    if count<=2:
        soma=soma+a
    a+=1
print(soma-1)

