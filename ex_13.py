lab = float(input('Digite a nota do trabalho de laboratório (0-10): '))
semestral = float(input('Digite a nota da avaliação semestral (0-10): '))
final = float(input('Digite a nota do exame final (0-10): '))
nota = (lab * 2 + semestral * 3 + final * 5) / 10
if 0 <= nota < 2.9:
    print('reprovado')
elif 3 <= nota < 4.9:
    print('em recuperação')
else:
    print('aprovado')