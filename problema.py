nome1 = input()
pontuacao1 = int(input())
nome2 = input()
pontuacao2 = int(input())
nome3 = input()
pontuacao3 = int(input())

if ((pontuacao1 < pontuacao2 and pontuacao1 < pontuacao3) or(pontuacao1 == pontuacao2 and pontuacao1 < pontuacao3) or (pontuacao1 == pontuacao3 and pontuacao1 < pontuacao2)):
    if (pontuacao2 < pontuacao3 and pontuacao1 != pontuacao2 and pontuacao1 != pontuacao3):
        print (f'{nome1} {pontuacao1}\n{nome2} {pontuacao2}\n{nome3} {pontuacao3}')
    elif (pontuacao3 < pontuacao2 and pontuacao1 != pontuacao2 and pontuacao1 != pontuacao3):
        print (f'{nome1} {pontuacao1}\n{nome3} {pontuacao3}\n{nome2} {pontuacao2}')
    elif (pontuacao2 == pontuacao3):
        if (len(nome2) < len(nome3)):
            print(f'{nome1} {pontuacao1}\n{nome2} {pontuacao2}\n{nome3} {pontuacao3}')
        elif (len(nome3) < len(nome2)):
            print(f'{nome1} {pontuacao1}\n{nome3} {pontuacao3}\n{nome2} {pontuacao2}')
    elif (pontuacao1 == pontuacao3):
        if (len(nome1) < len(nome3)):
            print(f'{nome1} {pontuacao1}\n{nome3} {pontuacao3}\n{nome2} {pontuacao2}')
        elif (len(nome3) < len(nome1)):
            print(f'{nome3} {pontuacao3}\n{nome1} {pontuacao1}\n{nome2} {pontuacao2}')
elif ((pontuacao2 < pontuacao1 and pontuacao2 < pontuacao3) or (pontuacao2 == pontuacao1 and pontuacao2 < pontuacao3) or (pontuacao2 == pontuacao3 and pontuacao2 < pontuacao1)):
    if (pontuacao1 < pontuacao3 and pontuacao2 != pontuacao1 and pontuacao2 != pontuacao3):
        print(f'{nome2} {pontuacao2}\n{nome1} {pontuacao1}\n{nome3} {pontuacao3}')
    elif (pontuacao3 < pontuacao1 and pontuacao2 != pontuacao1 and pontuacao2 != pontuacao3):
        print(f'{nome2} {pontuacao2}\n{nome3} {pontuacao3}\n{nome1} {pontuacao1}')
    elif (pontuacao1 == pontuacao3):
        if (len(nome1) < len(nome3)):
            print(f'{nome2} {pontuacao2}\n{nome1} {pontuacao1}\n{nome3} {pontuacao3}')
        elif (len(nome3) < len(nome1)):
            print(f'{nome2} {pontuacao2}\n{nome3} {pontuacao3}\n{nome1} {pontuacao1}')
    elif (pontuacao2 == pontuacao3):
        if (len(nome2) < len(nome3)):
            print(f'{nome2} {pontuacao2}\n{nome3} {pontuacao3}\n{nome1} {pontuacao1}')
        elif (len(nome3) < len(nome2)):
            print(f'{nome3} {pontuacao3}\n{nome2} {pontuacao2}\n{nome1} {pontuacao1}')
elif ((pontuacao3 < pontuacao1 and pontuacao3 < pontuacao2) or (pontuacao3 == pontuacao1 and pontuacao3 < pontuacao2) or  (pontuacao3 == pontuacao2 and pontuacao3 < pontuacao1)):
    if (pontuacao1 < pontuacao2 and pontuacao3 != pontuacao1 and pontuacao3 != pontuacao2):
        print(f'{nome3} {pontuacao3}\n{nome1} {pontuacao1}\n{nome2} {pontuacao2}')
    elif (pontuacao2 < pontuacao1 and pontuacao3 != pontuacao1 and pontuacao3 != pontuacao2):
        print(f'{nome3} {pontuacao3}\n{nome2} {pontuacao2}\n{nome1} {pontuacao1}')
    elif (pontuacao1 == pontuacao2):
        if (len(nome1) < len(nome2)):
            print(f'{nome3} {pontuacao3}\n{nome1} {pontuacao1}\n{nome2} {pontuacao2}')
        elif (len(nome2) < len(nome1)):
            print(f'{nome3} {pontuacao3}\n{nome2} {pontuacao2}\n{nome1} {pontuacao1}')
    elif (pontuacao2 == pontuacao3):
        if (len(nome2) < len(nome3)):
            print(f'{nome2} {pontuacao2}\n{nome3} {pontuacao3}\n{nome1} {pontuacao1}')
        elif (len(nome3) < len(nome2)):
            print(f'{nome3} {pontuacao3}\n{nome2} {pontuacao2}\n{nome1} {pontuacao1}')
elif (pontuacao1 == pontuacao2 == pontuacao3):
    if (len(nome1) <= len(nome2) and len(nome1) <= len(nome3)):
        print(f'{nome1} {pontuacao1}\n{nome2} {pontuacao2}\n{nome3} {pontuacao3}')
    elif (len(nome2) <= len(nome1) and len(nome2) <= len(nome3)):
        print(f'{nome2} {pontuacao2}\n{nome1} {pontuacao1}\n{nome3} {pontuacao3}')
    elif (len(nome3) < len(nome1) and len(nome3) < len(nome2)):
        print(f'{nome3} {pontuacao3}\n{nome1} {pontuacao1}\n{nome2} {pontuacao2}')
