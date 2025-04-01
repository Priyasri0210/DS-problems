#function definition
#Function call

#function definition syntax
#def <functionname>():
    #Logic

#Dynamic
#arguments
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

    print('Done')


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    operation = input()

    #function call
    calculator(a,b,operation)

    print('square of a')
    print(a**2)

    c = int(input())
    d = int(input())
    oper = input()

    #function call
    calculator(c,d,oper)
    
