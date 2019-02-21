# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input('Digite seu nome: ')

while (len(nome) < 3):
    nome = input('Nome muito curto, digite novamente: ')
else:
    idade = int(input('Digite sua idade: '))

    while (idade < 0 or idade > 150):
        idade = int(input('Idade inválida, digite novamente: '))
    else:
        salario = int(input('Digite seu salário: '))

        while (salario < 0):
            salario = int(input('Salario invalido, digite novamente: '))
        else:
            sexo = input('Digite seu sexo: ')

            while (sexo != "f" and sexo != "m"):
                sexo = input('Valor inválido, digite novamente: ')
            else: 
                ec = input('Digite seu estado civil: ')

                while (ec != 's' and ec != 'c' and ec != 'v' and ec != 'd'):
                    ec = input('Valor inválido, digite novamente: ')
                else:
                    print('Dados corretos, cadastro efetuado!')

    