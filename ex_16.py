bmaior = float(input('Digite a medida da base maior do trapézio em centímetros: '))
bmenor = float(input('Digite a medida da base menor do trapézio em centímetros: '))
altura = float(input('Digite a altura do trapézio em centímetros: '))
if bmaior <= 0 or bmenor <= 0 :
    print('digite uma medida valida ')
else:
    area = ((bmaior + bmenor) * 2)
    print(f'A área do trapezio é de {area} cm².')
