nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
media_pond = (nota1 + nota2 + nota2) / (1+2)
if media_pond >=7:
    print(f'Aluno aprovado!! A media é {media_pond}')
else:
    print(f'Aluno reprovado!! A média é {media_pond}')
