import math
largura = float(input(""))
altura = float(input(""))
custoLata = float(input(""))
rendimento = float(input(""))

tamanho = largura*altura
x = tamanho/rendimento
z = math.ceil(x)
y = custoLata*z

print(f"{z}")
print(f"{y:.2f}")
 

