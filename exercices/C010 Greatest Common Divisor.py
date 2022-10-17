a=int(input(""))
b=int(input(""))

anterior = a
atual = b
resto = anterior%atual
if resto == 0:
    print(atual)
else:
    while resto != 0:
        resto = anterior%atual
        anterior = atual
        atual = resto
    print(anterior)

    
