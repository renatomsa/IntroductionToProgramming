musica = input()
genero = input()

if (genero == 'Forró' or genero == 'Xote'):
    print (f"'{musica}' foi adicionada com sucesso na playlist 'Dandrilha'.")
else:
    print (f'Ocorreu um erro ao adicionar {musica} na playlist.')