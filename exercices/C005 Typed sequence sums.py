i=''
soma_par=0
soma_impar=0
soma_total=0
while i != 0:
    i = int(input(""))
    soma_total=soma_total+i
    if (i%2)==0:
            soma_par= soma_par+i
    elif (i%2)!=0:
        soma_impar= soma_impar+i
print(soma_par)
print(soma_impar)
print(soma_total)
