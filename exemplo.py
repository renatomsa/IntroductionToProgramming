import locale

print("Locutor: Espero que todo mundo se divirta bastante hoje")
nome_br = input ("Locutor: Vamos receber o representante brasileiro: ")
nome_us = input ("Locutor: Vamos receber o representante americano: ")

print(f'Locutor: O brasileiro {nome_br} vai contar sua piada!')
db_br = float(input('Sensor: digite o valor em decibéis medido para a piada do brasileiro: '))

locale.setlocale(locale.LC_ALL, 'pt_BR')

print('\nPainel: \n{}\n{} dB\n'.format(nome_br, locale.format_string('%.2f',db_br)))

print(f'Locutor: O americano {nome_us} vai contar sua piada! ')
db_us = float(input('Sensor: digite o valor em decibeis medido para a piada do americano: '))

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

print('\nPainel: \n{}\n{} dB\n' .format(nome_us, locale.format_string('%.2f',db_us)))

if(db_br > db_us):
    vencedor = 'Brasileiro'
    real_to_dolar = float(input('Sistema: digite o valor de conversão de real para dólar: '))
    valor_real = 10 * real_to_dolar
elif (db_br < db_us):
    vencedor = 'Americano'
else:
    vencedor = 'Empate'

if (vencedor == 'Empate'):
    print('\nPainel: \nTivemos um empate!')
elif (vencedor == 'Brasileiro'):
    print("\nPainel: \n O GRANDE VENCEDOR DA NOITE É")
    locale.setlocale(locale.LC_ALL, 'pt_BR')
    print('{}\nR$ {}' .format(nome_br,locale.format_string('%.2f',valor_real)))
elif (vencedor == 'Americano'):
    print("\nPainel: \n O GRANDE VENCEDOR DA NOITE É")
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    print('{}\nU$$ {}' .format(nome_br,locale.format_string('%.2f',10)))