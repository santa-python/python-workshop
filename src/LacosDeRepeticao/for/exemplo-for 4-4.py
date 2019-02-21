i = 0;
listaNumeros = [1,2,3,4,5,6,7,8,9,50]
numerosIncorretos = []
for n in listaNumeros:
    if(type(n) != int):
        aux = ""
        break
    if(n < 1 or n > 9):
        numerosIncorretos.append(n)
        del(listaNumeros[i])
        continue
    i+= 1
else:
    aux = " não"
    print("Numeros Invalidos retirados do Array:" + str(numerosIncorretos))
    print("Array percorrido:" + str(listaNumeros))

print("O Array"+ aux +" contem uma String")
#O Array contem uma String