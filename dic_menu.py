repetir='S'
con=0
d={}
while repetir=='S' or repetir=='s':
  l=[]
  nom=input('Ingrese el nombre: ')
  l.append(nom)
  edad=int(input('Ingrese el edad: '))
  l.append(edad)
  sexo=input('Ingrese el sexo: ')
  l.append(sexo)
  tel=int(input('Ingrese el Telefono: '))
  l.append(tel)
  email=input('Ingrese la dirección de correo: ')
  l.append(email)
  d[con]=l
  con+=1
  repetir=input('¿Desea continuar S/N?')

print(d)