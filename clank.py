def counting_open_parenthesis(expression):
    if (len(expression) == 0):
        return 0
    elif (expression[0] == "("):
        return 1 + counting_open_parenthesis(expression[1:])
    else:
        return counting_open_parenthesis(expression[1:])

def counting_close_parenthesis(expression):
    if (len(expression) == 0):
        return 0
    elif (expression[0] == ")"):
        return 1 + counting_close_parenthesis(expression[1:])
    else:
        return counting_close_parenthesis(expression[1:])

expressions_qty = int(input())

for i in range(expressions_qty):
    exp = input()
    open_p_counter = counting_open_parenthesis(exp)
    close_p_counter = counting_close_parenthesis(exp)

    if (open_p_counter == close_p_counter):
        print("Essa sentença está com os parênteses balanceados, HOORAY!")
    elif (open_p_counter > close_p_counter):
        print("A quantidade de parênteses '(' está maior que a de ')', vamos descartá-la")
    elif (open_p_counter < close_p_counter):
        print("A quantidade de parênteses ')' está maior que a de '(', vamos descartá-la")