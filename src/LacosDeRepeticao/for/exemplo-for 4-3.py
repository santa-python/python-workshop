listaNumeros = [1,2,3,4,5,6,7,8,9,18]
for n in listaNumeros:
    if(n < 1 or n > 9):
        msg = "Existem numeros invalidos nesse array"
        break
    print(n)
else:
    msg = "Array percorrido"
print(msg)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# Existem numeros invalidos nesse array