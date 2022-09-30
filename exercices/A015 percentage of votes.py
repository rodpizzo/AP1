import math
numeroEleitores = int(input(""))
votosBrancos = int(input(""))
votosNulos = int(input(""))
votosValidos = int(input(""))

nulos = (votosNulos/numeroEleitores)*100

brancos = (votosBrancos/numeroEleitores)*100

validos = (votosValidos/numeroEleitores)*100

ausentes = 100-(nulos+brancos+validos)

print(f"Nulos: {nulos:.2f}%")
print(f"Brancos: {brancos:.2f}%")
print(f"Validos: {validos:.2f}%")
print(f"Ausentes: {ausentes:.2f}%")




