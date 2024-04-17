import math

def calcular_preco(chegada, partida):

    minutos_chegada = chegada[0] * 60 + chegada[1]
    minutos_partida = partida[0] * 60 + partida[1]

    diferenca_minutos = minutos_partida - minutos_chegada

    numero_horas = math.ceil(diferenca_minutos / 60)

    if numero_horas <= 2:
        preco = numero_horas * 1.00
    elif numero_horas <= 4:
        preco = 2 * 1.00 + (numero_horas - 2) * 1.40
    else:
        preco = 2 * 1.00 + 2 * 1.40 + (numero_horas - 4) * 2.00

    return preco

def main():

    chegada = tuple(map(int, input('Digite a hora de chegada (hora minuto): ').split()))
    partida = tuple(map(int, input('Digite a hora de partida (hora minuto): ').split()))

    preco = calcular_preco(chegada, partida)

    print('O preço cobrado pelo estacionamento é R$', preco)

if __name__ == "__main__":
    main()