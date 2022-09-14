def fatorial(x):
    if x == 0:
        return 1
    else:
        return x *(fatorial (x-1))

random_str = input()

uppercase_str_lst = []
lowcase_str_lst = []

for i in random_str:
    if i.isupper() == True:
        uppercase_str_lst.append(i)
    else:
        lowcase_str_lst.append(i)

n = len(uppercase_str_lst) + len(lowcase_str_lst)

if len(uppercase_str_lst) < len(lowcase_str_lst):
    k = len(lowcase_str_lst)
else:
    k = len(uppercase_str_lst)

combnt = int((fatorial(n))/((fatorial(k))*(fatorial(n-k))))

selected_str = random_str[int((combnt % k))]

dmns_name = str(selected_str) + "-" + str(combnt)

if selected_str.isupper() == True:
    print(f"Morty!!! Morty!!! Vamos para a dimensão {dmns_name}, Morty!!! Vai ser legal, Morty!!! Rick e Morty na dimensão {dmns_name} para sempre, Morty!!! Wubba lubba dub dub!!!")
else:
    print(f"Oh geez, Rick!!! Eu não sei se ir pra dimensão {dmns_name} é uma boa ideia... Eu estou com medo, Rick!!! Oh geez!!!")
