mes_int = int(input('Digite o número do mes: '))
mes_str = ''
if mes_int == 1:
    mes_srt = 'Janeiro'
elif mes_int == 2:
    mes_srt = 'Fevereiro'
elif mes_int == 3:
    mes_srt = 'Março'
elif mes_int == 4:
    mes_srt = 'Abril'
elif mes_int == 5:
    mes_srt = 'Maio'
elif mes_int == 6:
    mes_srt = 'Junho'
elif mes_int == 7:
    mes_srt = 'Julho'
elif mes_int == 8:
    mes_srt = 'Agosto'
elif mes_int == 9:
    mes_srt = 'Setembro'
elif mes_int == 10:
    mes_srt = 'Outubro'
elif mes_int == 11:
    mes_srt = 'Novembro'
elif mes_int == 12:
    mes_srt = 'Dezembro'
else:
    print('mes inexistente')

print(f'O  correspondente é {mes_srt}')