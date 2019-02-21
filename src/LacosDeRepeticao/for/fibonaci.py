n = int(input('Quantos numeros da sequencia de finobaci gostaria de ver'))    
cont,y,x = 0,0,1
while(cont < n):   
    print(x)
    aux = x + y
    y = x
    x = aux
    cont+= 1


