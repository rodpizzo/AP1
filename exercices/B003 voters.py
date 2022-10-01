idade = int(input())
if idade >= 16 and idade <= 17:
        print("FACULTATIVO")

elif idade >= 18 and idade <=69:
        print("OBRIGATORIO")
elif idade < 16 and idade >= 70:
        print("DISPENSADO")
elif idade > 70:
    print("DISPENSADO")
elif idade < 16:
    print("DISPENSADO")
