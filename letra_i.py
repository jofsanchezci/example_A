palabra=input('Ingrese una palabra: ')
aux=palabra[::-1]
if palabra==aux:
	print('Es un palindromo')
else:
	print('No es palindromo')
