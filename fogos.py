nome_fogo = input()
quantidade_db_fogo = int(input())
db_caruaru = int(input())
db_campinagrande = int(input())

if (quantidade_db_fogo <= db_caruaru and quantidade_db_fogo <= db_campinagrande):
    print (f'Boa Felipe, o {nome_fogo} será um sucesso em Campina Grande e Caruaru!')
elif (quantidade_db_fogo <= db_caruaru and quantidade_db_fogo > db_campinagrande):
    print (f'Infelizmente em Campina Grande não vai rolar, mas em Caruaru o {nome_fogo} vai ser extouro!')
elif (quantidade_db_fogo <= db_campinagrande and quantidade_db_fogo > db_caruaru):
    print (f'Infelizmente em Caruaru não vai rolar, mas em Campina Grande o {nome_fogo} vai ser extouro!')
else:
    print (f'Poxa Felipe, não vai ser dessa vez que {nome_fogo} fará um sucesso pelas festas juninas do Brasil')