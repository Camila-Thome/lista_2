num1 = float(input('insira um numero: '))
num2 = float(input('insira um segundo numero: '))
dif1 = num1 - num2 
dif2 = num2 - num1
if (num1 <= num2):
    print(f'{num2} é maior que {num1} e a diferença entre eles é de {dif1} ')
else:
    print(f'{num1} é maior que {num2} e a diferença entre eles é de {dif2} ')
