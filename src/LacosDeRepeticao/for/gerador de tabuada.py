while(True):
    n = int(input('Qual tabuada entre 1 e 10 gostaria de ver'))
    if(n < 1 or n > 10):
        continue
    for i in range(11): 
        print(str(n) + ' X ' + str(i) + ' = ' + str((n*i)))
    break