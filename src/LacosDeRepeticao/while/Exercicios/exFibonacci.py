# Faça um programa capaz de gerar a sequencia de fibonacci a partir da quantidade de termos escolhida.

term = int(input('Digite a quantidade de termos: '))

term1 = 0
term2 = 1

print (term1)
print (term2)

cont = 3

while(cont <= term):
    term3 = term1 + term2
    print(term3)
    term1 = term2
    term2 = term3
    cont = cont + 1