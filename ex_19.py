a = float(input("Digite o comprimento do lado A do triângulo: "))
b = float(input("Digite o comprimento do lado B do triângulo: "))
c = float(input("Digite o comprimento do lado C do triângulo: "))
if a + c <= b or b + c <= a or  a + b <= c:
    print('não se encaixa como triangulo, minha flor!!')
elif a == b == c:
    print('é um triangulo equilatero, cimetrico igual seu bumbum!!')
elif a == b or a == c or b == c:
    print('é um triângulo isósceles, alto igual o menino que te iludiu!!')
else:
    print('é um triangulo escaleno, todo torto igual sua cara!!')