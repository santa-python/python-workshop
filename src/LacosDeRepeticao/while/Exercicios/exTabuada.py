# Escreva um programa que receba um número e faça a tabuada de 0 a 10 do mesmo.

mult = 0
num = int(input('Digite um numero: '))

while (mult <= 10):
    print('{} x {} = {}'.format(num, mult, mult*num))
    mult = mult + 1