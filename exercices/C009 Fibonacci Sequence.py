n= int(input())
a1=1
a2=1
i=0
a3=0
if n==0:
    print(0)
elif n==1:
    print(1)
else:
    print(a1, end=' ')
    print(a2, end=' ')
    while i<n-2:
        a3=(a1+a2)
        print(a3, end=' ')
        a1=a2
        a2=a3
        i+=1

