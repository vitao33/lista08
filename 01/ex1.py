def dizer_ola():
    print('Ola Mundo!')



def exibir_saidacoes(nome: str, periodo: int):
    if periodo == 1:
        print(f'Bom dia, {nome}')
    elif periodo == 2:
        print(f'Bom tarde, {nome}')
    else:
        print(f'Boa noite, {nome}')

dizer_ola()
exibir_saidacoes('Senhor Kanoff',3)
exibir_saidacoes(periodo=1, nome='José')
