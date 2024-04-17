import math
numero = int(input('insira um numero: '))
logaritmo = math.log
resultado = math.log(numero)
if numero > 0:
    logaritmo = math.log(numero)
    print("O logaritmo natural de", numero, "é:", logaritmo)
else:
    print("Por favor, digite um número válido.")
