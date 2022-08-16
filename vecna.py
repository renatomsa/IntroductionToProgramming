symptoms_predict = ['dor de cabeca', 'insonia', 'pesadelos', 'suor frio', 'visoes']
run = False
victims = []
while run == False:
    i = 0
    suspects_lst = input().split(', ')
    if suspects_lst[0] == 'descobrir':
        run = True
    suspects_lst_copy = suspects_lst.copy()
    suspects_lst_analyse = suspects_lst_copy.pop(0)
    for element in suspects_lst_copy:
        if element in symptoms_predict:
            i += 1
        if i == 5:
            victims.append(suspects_lst[0])
victims_number = len(victims)
if victims_number == 0:
    print('Não conseguimos encontrar ninguém com esses sintomas, o próximo ataque do Vecna será imprevisível.')
else:
    for find_max in victims:
        if find_max == 'Max':
            print('Oh não, Max está em perigo! Let\'s run up that hill com a Kate Bush e ajudar nossa amiga.')
            if victims_number > 1 and victims_number <= 2:
                print(f'Além dela, tem mais {victims_number - 1} pessoa(s) na mira do Vecna!')
                print(f'Precisamos avisar {victims} para preparar sua música favorita.')
            else:
                print(f'Além dela, tem mais {victims_number} pessoa(s) na mira do Vecna!')
                print('Precisamos avisar {victims} para prepararem suas músicas favoritas.'[1:])
        elif find_max != 'Max' and victims_number > 1 and victims_number <= 2:
            print(f'Além dela, tem mais {victims_number} pessoa(s) na mira do Vecna!')
            print(f'Precisamos avisar {victims} para preparar sua música favorita.')
        else:
            print(f'Além dela, tem mais {victims_number} pessoa(s) na mira do Vecna!')
            print(f'Precisamos avisar {victims} para prepararem suas músicas favoritas.')
