a = int(input())
b = int(input())
c = int(input())

#escaleno

if (a+b)<c or (b+c)<a or (a+c)<b:
    print("INVALIDO")
elif a==b==c:
    print("EQUILATERO")
elif a==b or a==c or b==c:
    print("ISOSCELES")
elif a != b != c:
    print("ESCALENO")
