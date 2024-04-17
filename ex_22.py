valor = float(input("Digite o valor do produto: "))
estado = input("Digite o estado destino do produto (MG, SP, RJ ou MS): ").upper()
impostos = {'MG': 0.07, 'SP': 0.12, 'RJ': 0.15, 'MS': 0.08}
if estado in impostos:
    taxa_imposto = impostos[estado]
    val_fin = valor * (1 + taxa_imposto)
    print(f'o valor final do produto será {val_fin} se for enviado para o estado {estado}')
else:
    print('há algo de errado :(! Digite informações válidas')
