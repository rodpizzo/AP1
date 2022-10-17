n = int(input(""))
divisor=1
total=0
while divisor<=n:
    total=total+(1/divisor)
    divisor+=1
print(f"{total:.4f}")
