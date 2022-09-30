segundos = int(input(""))

dias = segundos//86400
diasSobra = segundos%86400

horas = diasSobra//3600
horasSobra = diasSobra%3600

minutos = horasSobra//60
minutosSobra = horasSobra%60

segundos = minutosSobra//1

print(f"{dias} {horas} {minutos} {segundos}")
