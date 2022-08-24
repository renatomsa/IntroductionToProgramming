def separate(test_str):
    test_str_copy = test_str

    vow="aeiou"

    for i in test_str_copy:
        if i in vow:
            test_str_copy=test_str_copy.replace(i,"*")
    res=test_str_copy.split("*")

    word_within_lst = []
    l = 0

    for j in test_str:
        if j in vow:
            word_within = (str(res[l]) + str(j))
            word_within_lst.append(word_within)
            l += 1
    return word_within_lst

completed = False
hospital = "shichikokuyama"
counting = 0
counted_words = []
counting_hospital = 0
forming_hospital = ""

while not completed:
    counted_words = []
    counting_elements = 0
    word = input()
    if len(separate(word)) == 1 and separate(word)[0] in forming_hospital:
        print("Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.")
    elif word in hospital and len(separate(word)) == 1 and word not in forming_hospital:
        print(f"Lembrei! A sílaba {word} está no nome do hospital. Obrigada, Totoro!")
        counted_words.append(word)
    elif word in hospital:
        printed = 0
        not_print = False
        for k in separate(word):
            if k in forming_hospital:
                not_print = True
        if not not_print:
            print(f"A palavra {word} está toda no nome do hospital. Acertou em cheio, Totoro!")
            counted_words.append(word)
            printed = 1
        elif printed != 1:
            word_lst = separate(word)
            for k in word_lst:
                if k in hospital and k not in forming_hospital and len(k) > 1:
                    counted_words.append(k)
            if len(counted_words) == 1 and printed != 1:
                print(f"Lembrei! A sílaba {counted_words[0]} está no nome do hospital. Obrigada, Totoro!")
            elif len(counted_words) > 1 and printed != 1:
                print(f"Lembrei! As sílabas: ", end = "")
                print(', '.join(counted_words), end = " ")
                print(f"estão no nome do hospital. Obrigada, Totoro!")
            elif printed != 1:
                print("Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.")
    else:
        word_lst = separate(word)
        for k in word_lst:
            if k in hospital and k not in forming_hospital and k not in counted_words and len(k) > 1:
                counted_words.append(k)
        if len(counted_words) == 1:
            print(f"Lembrei! A sílaba {counted_words[0]} está no nome do hospital. Obrigada, Totoro!")
        elif len(counted_words) > 1:
            print(f"Lembrei! As sílabas: ", end = "")
            print(', '.join(counted_words), end = " ")
            print(f"estão no nome do hospital. Obrigada, Totoro!")
        else:
            print("Infelizmente nenhuma dessas sílabas me lembrou do nome do hospital, Totoro.")

    for forming in range(len(counted_words)):
        forming_hospital += counted_words[int(forming)]
    if len(forming_hospital) >= 14:
        completed = True

print("Conseguimos lembrar o nome do hospital shichikokuyama, agora é só pegar o Catbus e ir até lá!")
