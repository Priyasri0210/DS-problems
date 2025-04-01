#Do to some repetitive task - Loops

while True:
    a = input("Enter value 1 - ")
    b = input("Enter value 2 - ")

    a = int(a)
    b = int(b)
    print("Enter stop to close the application")
    operation = input("Enter operation - ")

    if operation == '+':
        c = a + b
        print("The addition value is " + str(c))
    elif operation == '-':
        c = a - b
        print("The Sub value is " + str(c))
    elif operation == '*':
        c = a * b
        print("The Mul value is " + str(c))
    elif operation == '/':
        c = a / b
        print("The Div value is " + str(c))
    elif operation == 'stop':
        break
    else:
        print('Not supported')

print('Done')



