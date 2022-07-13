#Meus stats
seu_nome = 'São João'

seus_pontos_vida = int(input())
seu_ataque = int(input())
sua_defesa = int(input())
sua_fraqueza = input()
sua_resistencia = input()

#Stats do adversário

nome_entidade = input()
pontos_vida_entidade = int(input())
ataque_entidade = int(input())
defesa_entidade = int(input())
fraqueza_entidade = input()
resistencia_entidade = input()

#Ataques por turno

ataque_1 = input()
# ataque_2 = input()
# ataque_3 = input()

#Ataques físicos

ataque_fisico_eu = (seu_ataque - defesa_entidade)
ataque_fisico_entidade = (ataque_entidade - sua_defesa)

#Ataques mágicos por mim

ataque_magia_resistencia_entidade = 0.5 * (seu_ataque - defesa_entidade)
ataque_magia_fraqueza_entidade = 1.7 * (seu_ataque - defesa_entidade)

#Ataques mágicos pela entidade

ataque_magia_resistencia_eu = 0.5 * (ataque_entidade - sua_defesa)
ataque_magia_fraqueza_eu = 1.7 * (ataque_entidade - sua_defesa)

# Primeira rodada (eu ataco)

numero_turno = 1
vida_restante_1 = (pontos_vida_entidade - ataque_fisico_eu)
vida_restante_1_magia_fraqueza = (pontos_vida_entidade - ataque_magia_fraqueza_entidade)
vida_restante_1_magia_resistencia = (pontos_vida_entidade - ataque_magia_resistencia_entidade)

if (ataque_1 == 'Ataque Físico' or fraqueza_entidade != 'fogo' or fraqueza_entidade != 'gelo' or fraqueza_entidade != 'eletricidade'):
    print(f'Turno: {numero_turno}\n{seu_nome} usou {ataque_1} e causou {ataque_fisico_eu} de dano em {nome_entidade} que agora tem {vida_restante_1} de vida')
elif (ataque_1 == 'Agi'):
    if (fraqueza_entidade == 'Agi'):
        print (f'Turno: {numero_turno}\nIsso! {seu_nome} usou {ataque_1} e acertou a fraqueza do adversário! A magia causou {ataque_magia_fraqueza_entidade} de dano em {nome_entidade} que agora tem {vida_restante_1_magia_fraqueza} de vida.')
    else:
        print (f'Turno: {numero_turno}\n{seu_nome} usou {ataque_1}, mas acertou uma resistência, portanto causou apenas {ataque_magia_resistencia_entidade} de dano em {nome_entidade} que agora tem {vida_restante_1_magia_resistencia} de vida.')
elif (ataque_1 == 'Bufu'):
    if (fraqueza_entidade == 'Bufu'):
        print (f'Turno: {numero_turno}\nIsso! {seu_nome} usou {ataque_1} e acertou a fraqueza do adversário! A magia causou {ataque_magia_fraqueza_entidade} de dano em {nome_entidade} que agora tem {vida_restante_1_magia_fraqueza} de vida.')
    else:
        print (f'Turno: {numero_turno}\n{seu_nome} usou {ataque_1}, mas acertou uma resistência, portanto causou apenas {ataque_magia_resistencia_entidade} de dano em {nome_entidade} que agora tem {vida_restante_1_magia_resistencia} de vida.')
elif (ataque_1 == 'Zio'):
    if (fraqueza_entidade == 'Zio'):
        print (f'Turno: {numero_turno}\nIsso! {seu_nome} usou {ataque_1} e acertou a fraqueza do adversário! A magia causou {ataque_magia_fraqueza_entidade} de dano em {nome_entidade} que agora tem {vida_restante_1_magia_fraqueza} de vida.')
    else:
        print (f'Turno: {numero_turno}\n{seu_nome} usou {ataque_1}, mas acertou uma resistência, portanto causou apenas {ataque_magia_resistencia_entidade} de dano em {nome_entidade} que agora tem {vida_restante_1_magia_resistencia} de vida.')

# Segunda rodada (caso aconteça) entidade ataca
vida_restante_final_1 = vida_restante_1 or vida_restante_1_magia_fraqueza or vida_restante_1_magia_resistencia
numero_turno = numero_turno + 1
vida_restante_2 = (seus_pontos_vida - ataque_fisico_entidade)
vida_restante_2_magia_fraqueza = (seus_pontos_vida - ataque_magia_fraqueza_eu)
vida_restante_2_magia_resistencia = (seus_pontos_vida - ataque_magia_resistencia_eu)

if (vida_restante_final_1 <= 0):
    print ('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
else:   
    if (fraqueza_entidade == ataque_1):
        print (f'{nome_entidade} teve sua fraqueza em {fraqueza_entidade} acertada, portanto não poderá agir.')
    else:
        ataque_2 = input()
        if (ataque_2 == 'Ataque Físico' or sua_fraqueza != 'fogo' or sua_fraqueza != 'gelo' or sua_fraqueza != 'eletricidade'):
            print(f'Turno: {numero_turno}\n{nome_entidade} usou {ataque_2} e causou {ataque_fisico_entidade} de dano em {seu_nome} que agora tem {vida_restante_2} de vida')
        elif (ataque_2 == 'Agi'):
            if (sua_fraqueza == 'Agi'):
                print (f'Turno: {numero_turno}\nVixe! {nome_entidade} usou {ataque_2} e acertou sua fraqueza! A magia causou {ataque_magia_fraqueza_entidade} de dano em {seu_nome} que agora tem {vida_restante_2_magia_fraqueza} de vida.')
            else:
                print (f'Turno: {numero_turno}\n{nome_entidade} usou {ataque_2}, mas acertou uma resistência, portanto causou apenas {ataque_magia_resistencia_entidade} de dano em {seu_nome} que agora tem {vida_restante_2_magia_resistencia} de vida.')
        elif (ataque_2 == 'Bufu'):
            if (sua_fraqueza == 'Bufu'):
                print (f'Turno: {numero_turno}\nVixe! {nome_entidade} usou {ataque_2} e acertou sua fraqueza! A magia causou {ataque_magia_fraqueza_entidade} de dano em {seu_nome} que agora tem {vida_restante_2_magia_fraqueza} de vida.')
            else:
                print (f'Turno: {numero_turno}\n{nome_entidade} usou {ataque_2}, mas acertou uma resistência, portanto causou apenas {ataque_magia_resistencia_entidade} de dano em {seu_nome} que agora tem {vida_restante_2_magia_resistencia} de vida.')
        elif (ataque_2 == 'Zio'):
            if (sua_fraqueza == 'Zio'):
                print (f'Turno: {numero_turno}\nVixe! {nome_entidade} usou {ataque_2} e acertou sua fraqueza! A magia causou {ataque_magia_fraqueza_entidade} de dano em {seu_nome} que agora tem {vida_restante_2_magia_fraqueza} de vida.')
            else:
                print (f'Turno: {numero_turno}\n{nome_entidade} usou {ataque_2}, mas acertou uma resistência, portanto causou apenas {ataque_magia_resistencia_entidade} de dano em {seu_nome} que agora tem {vida_restante_2_magia_resistencia} de vida.')


# Última rodada (caso aconteça) eu ataco
vida_restante_final_2 = vida_restante_2 or vida_restante_2_magia_fraqueza or vida_restante_2_magia_resistencia
numero_turno = numero_turno + 1
vida_restante_3 = (vida_restante_final_1 - ataque_fisico_eu)
vida_restante_3_magia_fraqueza = (vida_restante_final_1 - ataque_magia_fraqueza_entidade)
vida_restante_3_magia_resistencia = (vida_restante_final_1 - ataque_magia_resistencia_entidade)


if (vida_restante_final_2 <= 0):
    print (f'Morremos… Parece que {nome_entidade} tem mais chances de ascender ao trono da Midsommar…')
else:
    ataque_3 = input()
    if (sua_fraqueza == ataque_2):
        print (f'{seu_nome} teve sua fraqueza em {sua_fraqueza} acertada, portanto não poderá agir.')
    else:
        if (ataque_3 == 'Ataque Físico' or fraqueza_entidade != 'fogo' or fraqueza_entidade != 'gelo' or fraqueza_entidade != 'eletricidade'):
            print(f'Turno: {numero_turno}\n{seu_nome} usou {ataque_3} e causou {ataque_fisico_eu} de dano em {nome_entidade} que agora tem {vida_restante_3} de vida')
        elif (ataque_3 == 'Agi'):
            if (fraqueza_entidade == 'Agi'):
                print (f'Turno: {numero_turno}\nIsso! {seu_nome} usou {ataque_3} e acertou a fraqueza do adversário! A magia causou {ataque_magia_fraqueza_entidade} de dano em {nome_entidade} que agora tem {vida_restante_3_magia_fraqueza} de vida.')
            else:
                print (f'Turno: {numero_turno}\n{seu_nome} usou {ataque_3}, mas acertou uma resistência, portanto causou apenas {ataque_magia_resistencia_entidade} de dano em {nome_entidade} que agora tem {vida_restante_3_magia_resistencia} de vida.')
        elif (ataque_3 == 'Bufu'):
            if (fraqueza_entidade == 'Bufu'):
                print (f'Turno: {numero_turno}\nIsso! {seu_nome} usou {ataque_3} e acertou a fraqueza do adversário! A magia causou {ataque_magia_fraqueza_entidade} de dano em {nome_entidade} que agora tem {vida_restante_3_magia_fraqueza} de vida.')
            else:
                print (f'Turno: {numero_turno}\n{seu_nome} usou {ataque_3}, mas acertou uma resistência, portanto causou apenas {ataque_magia_resistencia_entidade} de dano em {nome_entidade} que agora tem {vida_restante_3_magia_resistencia} de vida.')
        elif (ataque_3 == 'Zio'):
            if (fraqueza_entidade == 'Zio'):
                print (f'Turno: {numero_turno}\nIsso! {seu_nome} usou {ataque_3} e acertou a fraqueza do adversário! A magia causou {ataque_magia_fraqueza_entidade} de dano em {nome_entidade} que agora tem {vida_restante_3_magia_fraqueza} de vida.')
            else:
                print (f'Turno: {numero_turno}\n{seu_nome} usou {ataque_3}, mas acertou uma resistência, portanto causou apenas {ataque_magia_resistencia_entidade} de dano em {nome_entidade} que agora tem {vida_restante_3_magia_resistencia} de vida.')

# Finalização

vida_restante_final_3 = vida_restante_3 or vida_restante_3_magia_fraqueza or vida_restante_3_magia_resistencia

if (vida_restante_final_3 <= 0):
    print ('Vitória! Parece que o Nahobino São João reinará nesse solstício!')
else:
    print ('Ambos ainda sobrevivem. Melhor se retirar e derrotar entidades mais fracas para ficar mais forte…')
