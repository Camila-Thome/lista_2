import math
numero = float(input('digite um numero: '))
if (numero >= 0):
     quadrado = numero * numero
     raiz = math.sqrt(numero)
     print(f'{numero} ao quadrado é igual a: {quadrado}. E a raiz quadrada de {numero} é : {raiz}')
else:
    print('numero invalido, tente novamente')