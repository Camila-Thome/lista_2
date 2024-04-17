salario = float(input('Insira o salario do trabalhador em reais:  '))
prestacao = float(input('Digite o valor da prestação do empréstimo: '))
valprest = salario * 0.20
if prestacao >= valprest:
    print("Empréstimo não concedido")
else:
     print("Empréstimo concedido")