#scope of a variable

# #Global variables
# #it will be alive till end of a program
# a = 10
# def greet():
#     #if a variable is created inside a function, it will alive
#     #untill inside the function
#     #Local variable
#     print(a)
#     value = 'Hello all'
#     print(value)

# #global variables
# b = 'bharath'
# greet()
# print('Done')
# print(a)
# print(b)
# print(value)

def calculator(val1, val2, opera):
    if opera == '+':
        #c is local variable
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

    #This return helps to send the value of local variable outside the function
    return c
    # print('Done')

a = int(input())
b = int(input())
operation = input()

#function call
#output is global
#Get the local variable value and store in global varaible
output = calculator(a,b,operation)

print('square of a')
print(output**2)