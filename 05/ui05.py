from area05 import *


def opcao_valida(opcao: int) -> bool:
    return opcao in (1, 2, 3)


def obeter_opcao() -> int:
    opcao = 0
    while not opcao in (1, 2, 3):
        print('** Menu de Opções **\n'
              '1 - Área do Quadrado\n'
              '2 - Área do Círculo\n'
              '3 - Área do Triângulo\n')
        opcao = int(input('==> '))

        if opcao not in (1, 2, 3):
            print('** Opção inválida, tente novamente **')

    return opcao
