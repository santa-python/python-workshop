# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor 
# seja inválido e continue pedindo até que o usuário informe um valor válido.

# Pede para o usuário digitar a nota.
nota = int(input('Digite o valor da nota: ')) 

# Enquanto a nota for menor que 0 ou maior que 10...
while (nota < 0 or nota > 10):
    # ... peça que digite a nota novamente.
    nota = int(input('Valor inválido! A nota deve estar entre 0 e 10. Digite novamente: ')) 

print('Valor válido. Nota = {}'.format(nota))