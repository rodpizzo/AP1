num=int(input(""))
i=1
x=0
count=0
while i<=num:
    x=num%i
    y=num%1
    if x==0 and y==0:
        count=count+1
    i+=1
    
if count>2:
    print("0")
else:
    print("1")
