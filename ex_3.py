import math
num = float(input('digite um numero: '))
if (num >= 0):
    raiz = math.sqrt(num)
    print(f'a raiz quadrada de {num} é : {raiz}')
else: 
  result = num * num
  print('o numero elevado ao quadrado é: ', result)