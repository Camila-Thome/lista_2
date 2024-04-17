import math
num = float(input('digite um numero: '))
if (num >= 0):
    raiz = math.sqrt(num)
    print(f'a raiz quadrada de {num} é : {raiz}')
else: 
    print('numero invalido, tente novamente')