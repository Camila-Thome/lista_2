idade = int(input('digite a idade do trabalhador em anos: '))
contribuicao = int(input('digite o tempo de trabalho/contribuição: '))
if idade >= 65:
    print('Aposentadoria aprovada!!')
elif contribuicao >= 30:
    print('Aposentadoria aprovada!!')
elif idade >= 60 and contribuicao >= 25:
    print('Aposentadoria aprovada!!')
else:
    print('aposentadoria negada')