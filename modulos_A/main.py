import paquete1
from paquete1 import resta

x=float(input('Ingrese numero x: '))
y=float(input('Ingrese numero y: '))

print(paquete1.suma(x,y), 'Esta es la suma')
print(resta(x,y), 'Esta es la resta')
print(paquete1.mul(x,y), 'Esta es la multiplicación')
print(paquete1.div(x,y), 'Esta es la división')
print(paquete1.raiz2(x), 'Esta es la raiz cuadrada')

