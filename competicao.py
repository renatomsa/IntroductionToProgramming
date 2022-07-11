nome_quadrilha = input()
passo1 = input()
passo2 = input()
passo3 = input()
passo4 = input()
passo5 = input()

passos_permitidos = 'Cumprimento' or 'Balancê' or 'Passeio' or 'Túnel' or 'Serrote' or 'Casamento' or 'Despedida'


if (passo1 == 'Cumprimento'):
    pontuacao1 = 100
elif (passo1 == 'Balancê'):
    pontuacao1 = 50
elif (passo1 == 'Passeio'):
    pontuacao1 = 70
elif (passo1 == 'Serrote'):
    pontuacao1 = 100
elif (passo1 == 'Casamento'):
    pontuacao1 = 0
else:
    pontuacao1 = 99999999

if (passo2 == 'Cumprimento'):
    pontuacao2 = pontuacao1 + 10
elif (passo2 == 'Balancê'):
    pontuacao2 = pontuacao1 + 50
elif (passo2 == 'Passeio'):
    pontuacao2 = pontuacao1 + 70
elif (passo2 == 'Túnel'):
    pontuacao2 = (pontuacao1 - 0.1 * pontuacao1)
elif (passo2 == 'Serrote'):
    pontuacao2 = pontuacao1 + 100
elif (passo2 == 'Casamento'):
    pontuacao2 = pontuacao1 + 0
else:
    pontuacao2 = 99999999

if (passo3 == 'Cumprimento'):
    pontuacao3 = pontuacao2 + 10
elif (passo3 == 'Balancê'):
    pontuacao3 = pontuacao2 + 50
elif (passo3 == 'Passeio'):
    pontuacao3 = pontuacao2 + 70
elif (passo3 == 'Túnel'):
    pontuacao3 = pontuacao2 + (pontuacao2 - 0.1 * pontuacao2)
elif (passo3 == 'Serrote'):
    pontuacao3 = pontuacao2 + 100
elif (passo3 == 'Casamento'):
    pontuacao3 = pontuacao2 + 0
else:
    pontuacao3 = 99999999

if (passo4 == 'Cumprimento'):
    pontuacao4 = pontuacao3 + 10
elif (passo4 == 'Balancê'):
    pontuacao4 = pontuacao3 + 50
elif (passo4 == 'Passeio'):
    pontuacao4 = pontuacao3 + 70
elif (passo4 == 'Túnel'):
    pontuacao4 = pontuacao3 + (pontuacao3 - 0.1 * pontuacao3)
elif (passo4 == 'Serrote'):
    pontuacao4 = pontuacao3 + 100
elif (passo4 == 'Casamento'):
    pontuacao4 = pontuacao3 + 0
else:
    pontuacao4 = 99999999

if (passo5 == 'Cumprimento'):
    pontuacao5 = pontuacao4 + 10
elif (passo5 == 'Balancê'):
    pontuacao5 = pontuacao4 + 50
elif (passo5 == 'Passeio'):
    pontuacao5 = pontuacao4 + 70
elif (passo5 == 'Túnel'):
    pontuacao5 = pontuacao4 + (pontuacao4 - 0.1 * pontuacao4)
elif (passo5 == 'Serrote'):
    pontuacao5 = pontuacao4 + 100
elif (passo5 == 'Casamento'):
    pontuacao5 = pontuacao4 + 0
elif (passo5 == 'Despedida'):
    pontuacao5 = pontuacao4 + 35
else:
    pontuacao5 = 99999999

passos_validacao = passo1 and passo2 and passo3 and passo4 and passo5

if (passo1 == 'Casamento' or passo2 == 'Casamento' or passo3 == 'Casamento' or passo4 == 'Casamento' or passo5 == 'Casamento'):
    pontuacao_final = pontuacao5 * 2
else:
    pontuacao_final = pontuacao5

if (pontuacao_final > 9999):
    print (f'Poxa, {nome_quadrilha}. Por utilizarem de algum passo não permitido vocês tiveram a pontuação zerada.')
else:
    print (f'Parabéns, {nome_quadrilha}! Bela apresentação. A pontuação foi de {pontuacao_final:.1f}!')