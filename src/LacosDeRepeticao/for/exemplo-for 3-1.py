# Vetor de vetores.

nomes = ["Joao","Maria", "Jose"]
idades = [18,20,17]
sexo = ['M','F','M']
tabela = [nomes, idades, sexo]

for linha in tabela:
    for coluna in linha:
        print(coluna)
