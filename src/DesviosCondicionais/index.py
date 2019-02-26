print('CONDICIONAIS', 'Comparação com dois numeros e verficar qual é o maior numero','', sep='\n')
x = input('Entre com o primeiro número qualquer: ')
y = input('Entre com o segundo número qualquer: ')

if x > y:
	print('O primeiro numero que foi {} foi maior que o segundo numero, que foi {}'.format(x,y))
else:
	print('O segundo numero que foi {} foi maior que o primeiro numero, que foi {}'.format(y,x))