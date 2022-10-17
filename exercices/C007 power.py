a=int(input(""))
if a>=0:
    b=int(input(""))
    if b>=0:
        if b%2==0:
            i=2
            total=1
            while i<=(b):
                total=total*(a*a)
                i+=2
        else:
            i=2
            total_impar=1
            while i<(b):
                total_impar=total_impar*(a*a)
                i+=2
            
            total=(total_impar)*a
       

        print(total)
        
    else:
        print('')
        
else:
    print('')
    
