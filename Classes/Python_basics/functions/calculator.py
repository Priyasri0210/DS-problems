def calculator(val1, val2, opera):
    if opera == '+':
        c = val1 + val2
        print("The addition value is " + str(c))
    elif opera == '-':
        c = val1 - val2
        print("The Sub value is " + str(c))
    elif opera == '*':
        c = val1 * val2
        print("The Mul value is " + str(c))
    elif opera == '/':
        c = val1 / val2
        print("The Div value is " + str(c))
    else:
        print('Not supported')
    return c
    print('Done')