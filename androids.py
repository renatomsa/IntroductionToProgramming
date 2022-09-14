def sum_digits (number):
    if number == 0:
        return 0
    return (number % 10 + sum_digits(int(number/10)))

def gcd_euclides_algorithm (n1, n2):
    if n2 == 0:
        return n1
    return gcd_euclides_algorithm(n2, n1 % n2)

num1 = int(input())
num2 = int(input())
num3 = int(input())

s_num1 = sum_digits(num1)
s_num2 = sum_digits(num2)
s_num3 = sum_digits(num3)

if s_num1 >= s_num2:
    gcd1 = gcd_euclides_algorithm(s_num1, s_num2)
elif s_num1 <= s_num2:
    gcd1 = gcd_euclides_algorithm(s_num2, s_num1)

if gcd1 >= s_num3:
    gcd = gcd_euclides_algorithm(gcd1, s_num3)
elif gcd1 <= s_num3:
    gcd = gcd_euclides_algorithm(s_num3, gcd1)

print(f"O MDC obtido é: {gcd}")