#Funcio de la recta
import matplotlib.pyplot as plt

def linea(x):
  return x

def cuadrado(x):
  return x**2
l=[]
m=[]
for i in range(-3,4):
  l.append(linea(i))
  m.append(cuadrado(i))

print(m)

plt.plot(l,l)
plt.plot(l,m)
plt.grid()
plt.show()