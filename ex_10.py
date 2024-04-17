def som_alg(num):
    soma = 0
    for algarismo in str(num):
        soma += int(algarismo)
    return soma
def main():
    num = int(input('Digite um número inteiro maior que zero: '))
    if num <= 0:
        print('Número inválido')
        return
    result = som_alg(num)
    print('A soma dos algarismos do número é: ', result)
if __name__ == "__main__":
    main()