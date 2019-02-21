n = int(input('Quantos numeros da sequencia de finobaci gostaria de ver'))    
y,x = 0,1
for a in range(n):
    print(x)
    aux = x + y
    y = x
    x = aux


