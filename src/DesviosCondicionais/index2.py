print('CONDICIONAL', 'Entrar com três numeros distintos e verificar qual é o maior', '', sep='\n')

x = input('Entre com o primeiro numero: ')
y = input('Entre com o segundo numero: ')
z = input('Entre com o terceiro numero: ')

if x > y:
	if x > z:
		print('o primeiro numero, o numero {}, é o maior!'.format(x))
elif y > z:
	print('o segundo numero, o numero {}, é o maior!'.format(y))
else:
	print('o terceiro numero, o numero {}, é o maior!'.format(z))