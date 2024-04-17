nota1 = float(input('digite a primeira nota com valor valido de 0.0 até 10.0: '))
nota2 = float(input('digite a segunda nota com valor valido de 0.0 até 10.0: '))
if 0.0 <= nota1 <= 10.0 and 0.0 <= nota2 <= 10.0:
    media = (nota1 + nota2) / 2
    print('a media final é: ', media)
else:
     print('Notas inválidas! As notas devem estar entre 0.0 e 10.0.')
