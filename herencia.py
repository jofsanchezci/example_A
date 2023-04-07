#Ejemplo de herencia

#------------------------------------------------------------------
#Se crean las clases
class Persona:
  def __init__(self):
    self.nombre=input('Ingrese el nombre: ')
    self.edad=int(input('Ingrese la edad: '))
    self.id=int(input('Ingrese el ID: '))
  
  def mostrar(self):
    print('Nombre: ', self.nombre)
    print('Edad: ', self.edad)
    print('ID: ', self.id)

#------------------------------------------------------------------
#Se crea la clase empleado
class Empleado(Persona):
  def __init__(self):
    #Se usa super() para hacer referencia al padre
    super().__init__()
    self.sueldo=float(input('Ingrese el sueldo: '))

  def mostrar(self):
    super().mostrar()
    print('El sueldo es: ', self.sueldo)
  
  def impuestos(self):
    if self.sueldo>5:
      print('Se debe Pagar impuestos')
    else:
      print('NO se debe Pagar impuestos')

#------------------------------------------------------------------
# Se instancia los diferentes objetos
persona=Persona()
persona.mostrar()


