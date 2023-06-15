from area05 import*
from ui05 import *
opcao = obeter_opcao()

if opcao == 1:
    lado = float(input('Informe o valor do lado: '))
    area = calcular_quadrado(lado)
elif opcao == 2:
    raio = float(input('Informe o valor do raio: '))
else:
    base = float(input('Informe o valor da base: ' ))
    altura = float(input('Informe o valor da base: ' ))
    area = calcular_triangulo(base, altura)
    print(f'A área é de {area}')