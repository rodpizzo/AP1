# ENTRADA:
x = int(input())
y = int(input())
z = int(input())
a=0
b=0
c=0

# PROCESSAMENTO:
#menor numero
if x<=y and x<=z:
    a=x
elif y<=x and y<=z:
    a=y
elif z<=x and z<=y:
    a=z
#maior numero
if z>=x and z>=y:
    c=z
elif x>=z and x>=y:
    c=x
elif y>=z and y>=x:
    c=y
#numero do meio
if x>=y and x<=z:
    b=x
elif y>=x and y<=z:
    b=y
elif z>=x and z<=y:
    b=z

# SAIDA:
print(a)
print(b)
print(c)
