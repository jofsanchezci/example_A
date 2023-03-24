#Factorial recursivo
def factoR(n):
  if n==0 or n==1:
    return 1
  else:
    return n*factoR(n-1)

for i in range(11):
  print('El Factorial de', i, 'es', factoR(i))