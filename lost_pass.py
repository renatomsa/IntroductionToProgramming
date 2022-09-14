def fatorial(x):
    if x == 0:
        return 1
    else:
        return x *(fatorial (x-1))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


password = input()
words_qty = int(input())
find = False

abc  = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for word in range(words_qty):
    new_pass = []
    pass_try = input()
    for letter in pass_try:
        letter_idx = (abc.index(letter) % 11)
        fibo_lst = []
        fatorial_lst = []

        for k in range(letter_idx):
            fibo_lst.append(fibonacci(k))
            fatorial_lst.append(fatorial(k))
        if (letter_idx == 0):
            new_pass.append("1")
        elif (letter_idx % 2 != 0):
            for number in range(len(fibo_lst)):
                abc_match = fibo_lst[number] * fatorial_lst[number]
                new_pass.append(abc[abc_match % 26])
        elif (letter_idx % 2 == 0):
            for number in range(len(fibo_lst)):
                abc_match = fibo_lst[number] + fatorial_lst[number]
                new_pass.append(abc[abc_match % 26])
    
    new_pass_str = ''.join(new_pass)
    if new_pass_str == password:
        print("Achamos! Achamos a senha.")
        find = True


if not find:
    print("É... Temos que procurar mais.")    