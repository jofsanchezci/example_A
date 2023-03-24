print('Ingrese los datos ')
nom=input('Ingrese el Nombre:')
edad=int(input('Ingrese el Edad: '))
dir=input('Ingrese el Direccion: ')
tel=int(input('Ingrese el numero de Tel: '))
d={'Nombre':'','Edad':'','Dir':'','Tel':''}
d['Nombre']=nom
d['Edad']=edad
d['Dir']=dir
d['Tel']=tel

x=d['Nombre']
y=d['Edad']
z=d['Dir']
q=d['Tel']

print(x,'tiene', y, 'años','vive en',z, 'su numero de telefono es', q)