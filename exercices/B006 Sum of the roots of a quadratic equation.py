import math
a = float(input())
b = float(input())
c = float(input())

delta = (b*b)-4*a*c

if delta < 0:
    print(math.nan)
elif delta >= 0:
    x1 = (-b+(delta**(1/2)))/2*a
    x2 = (-b-(delta**(1/2)))/2*a
    somaraiz = x1+x2
    print(f"{somaraiz:.2f}")
elif delta == 0:
    x = -b/2*a
    print(f"{x:.2f}")
