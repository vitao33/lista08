from começo import *
from segunda import *
opcao = 0
while opcao != 3:
    opcao = obter_opcao()

    if opcao == 1:
        tratar_combinacao()
    elif opcao == 2:
        tratar_arranjo()
    elif opcao != 3:
        print('Opção inválida!!!')
