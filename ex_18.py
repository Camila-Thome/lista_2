numero = int(input("Digite um número inteiro: "))
if numero % 3 == 0 and numero % 5 == 0:
   print('não divisivel por 3 e 5 simultaneamente')
elif numero % 3 == 0:
    print('divisivel por 3')
elif numero % 5 == 0:
    print('divisivel por 5')
else:
    print ('não divisivel por nenhum dos divisores')
    