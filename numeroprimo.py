#Numero primos
num=int(input('Ingrese el numero a evaluar: '))
cont=0

for i in range(1,num+1):
  if num%i==0:
    cont+=1

if cont ==2:
  print('El numero es primo')
else:
  print('El numero NO es primo')
