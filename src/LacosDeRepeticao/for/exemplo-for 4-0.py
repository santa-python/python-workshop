#Tira todas as letras 'a' da frase

frase = "Eu gosto de fadas"
novaFrase = ""
for letra in frase:
    if(letra == "a"):
        continue
    novaFrase += letra
print(novaFrase)

#Eu gosto de fds