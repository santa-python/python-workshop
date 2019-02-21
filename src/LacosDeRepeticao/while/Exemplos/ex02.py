# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome 
# do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')

while (senha == nome):
    senha = input('A senha não pode ser igual ao nome de usuário! Digite a senha novamente: ')

print('Cadastrado com sucesso!')