import os

restaurante = [
    {'nome':'Praça','categoria':'Japonesa','ativo':False},
    {'nome':'Dogão','categoria':'Lanche','ativo':True},
    {'nome':'Nossa massa','categoria':'Italiana','ativo':True}
]

def exibir_nome_do_app():
    print('Blessed Food\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar Restaurantes')
    print('4. Sair')

def finalizar_app():
    exibir_subtitulo('App finalizado')

def main():
    os.system('cls')
    exibir_nome_do_app()
    exibir_opcoes()
    escolher_opcao()

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    print('Opção Invalida!')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastrar novo restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar:  ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {
        'nome': nome_do_restaurante,
        'categoria': categoria,
        'ativo': False
    }
    restaurante.append(dados_do_restaurante)
    print(f'O restaurante: {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def listar_restaurante():
    exibir_subtitulo('Listar restaurantes')

    for nome in restaurante:
        nome_restaurante = nome['nome']
        categoria = nome['categoria']
        ativo = nome['ativo']
        print(f'- {nome_restaurante} | {categoria} | {ativo}')

    voltar_ao_menu_principal()

def alterar_estado_do_restaurante():
    exibir_subtitulo('Alterar estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for r in restaurante:
        if nome_restaurante == r['nome']:
            restaurante_encontrado = True
            r['ativo'] = not r['ativo']
            mensagem = (
                f'O restaurante {nome_restaurante} foi ativado com sucesso!'
                if r['ativo']
                else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            )
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            alterar_estado_do_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

if __name__ == '__main__':
    main()
