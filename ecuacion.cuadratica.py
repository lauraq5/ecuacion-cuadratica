# programa para calcular uan ecuacion cuadratica 

import math 


print("------------------------------------------")
print("---- Resolver la ecuacion cuadrática------")
print("------------------------------------------")

# input 

a = int(input("Digite el valor de  a: "))
b = int(input("Digite el valor de  b: "))
c = int (input("Digite el valor de c: "))

# processing

d = b**2-4*a*c
if d == 0:
    x1 = (d/2*a)
    x2 = x1
    print(x1, x2)
if d > 0:
    x1 =(-b+math.sqrt(d))/(2*a)
    x2 =(-b-math.sqrt(d))/(2*a)
    print(x1, x2)
else: 
    print("la solucion es imaginaria")
    