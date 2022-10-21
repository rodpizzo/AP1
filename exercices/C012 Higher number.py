tamanho = int(input(""))
i=0
num=0
count=0
while i<tamanho:
    num=int(input(""))
    i+=1
    if num >= count:
        count=num
print(count)
        
