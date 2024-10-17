def introduction_page():
    message = '''
        Sistema Cadastral

        1. Cadastrar Pessoa
        2. Buscar pessoa por nome
        5. Sair
    '''

    print(message)
    command = input('Comando: ')
    return command