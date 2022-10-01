limiteVelocidade = int(input(""))
multa = float(input(""))
multaExtra =float(input(""))
velocidade = float(input(""))

if velocidade > limiteVelocidade:
    calculoMulta1 = (velocidade-limiteVelocidade)*multaExtra
    calculoMultaT = calculoMulta1+multa
    print(f"{calculoMultaT:.2f}")
else:
    print("0.00")

