# Receba um numero e calcule o fatorial dele.

num = int(input('Digite um numero para calcular o fatorial: '))
cont = num
fat = 1

# Continua até 
while(cont > 0):
    fat *= cont
    cont -= 1

print('O fatorial de {} é {}'.format(num, fat))
