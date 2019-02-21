nomes = ["Joao","Maria", "Jose"]
idades = [18,20,17]
sexo = ['M','F','M']
tabela = [nomes,idades,sexo]

for i in range(3):
        for j in range(3):
                print(tabela[j][i], end=" ")
        print(" ")

# Joao 18 M  
# Maria 20 F  
# Jose 17 M  