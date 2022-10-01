limiteKm = int(input())
tarifa1= float(input())
tarifa2= float(input())
quantKm= float(input())

if quantKm <= limiteKm:
    valor= tarifa1*quantKm
    print(f"{valor:.2f}")
else:
    valor= tarifa2*quantKm
    print(f"{valor:.2f}")
    
