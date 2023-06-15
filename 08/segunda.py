from começo import *
def obter_opcao() -> int:
    print('** Menu de Opções ** \n'
          '1 - Calcular Cobinações\n'
          '2 - Calcular Arranjo\n'
          '3 - Sair')



    return int(input('==>'))




def tratar_combinacao():
    n = int(input('Informe o número de elementos (n):'))
    p = int(input('Informe o tamanho dos agrupamentos (p): '))

    result = calcular_combinacoes(n, p)
    print(f'O total de combinações é {result:.1f}')

def tratar_arranjo():
    n = int(input('Informe o número de elementos (n):'))
    p = int(input('Informe o tamanho dos agrupamentos (p): '))

    result = tratar_arranjo(n, p)
    print(f'O total de arranjo é {result:.1f}')
