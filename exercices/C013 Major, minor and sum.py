tamanho = int(input(""))
i=1
num=0

num=int(input(""))
countmaior=num
countmenor=num
soma=num
while i<tamanho:
    num=int(input(""))
    i= i+1
    soma=soma+num
    if num >= countmaior:
        countmaior=num
    if num <= countmenor:
        countmenor=num
    
    
print(countmaior)
print(countmenor)
print(soma)
