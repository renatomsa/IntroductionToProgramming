cidade1 = input()
nota1 = float(input())
distancia1 = int(input())

cidade2 = input()
nota2 = float(input())
distancia2 = int(input())

cidade3 = input()
nota3 = float(input())
distancia3 = int(input())

if (nota1 >= 4 or nota2 >= 4 or nota3 >= 4):
    if (nota1 > nota2 and nota1 > nota3):
        print (f'{cidade1}')
    elif (nota2 > nota1 and nota2 > nota3):
        print (f'{cidade2}')
    elif (nota3 > nota1 and nota3 > nota2):
        print (f'{cidade3}')
    elif (nota1 == nota2 or nota1 == nota3 or nota2 == nota3 or nota1 == nota2 == nota3):
        if (distancia1 < distancia2 and distancia1 < distancia3):
            print (f'{cidade1}')
        elif (distancia2 < distancia1 and distancia2 < distancia3):
            print (f'{cidade2}')
        elif (distancia3 < distancia1 and distancia3 < distancia2):
            print (f'{cidade3}')
else:
    print ('Nota mínima não atingida')