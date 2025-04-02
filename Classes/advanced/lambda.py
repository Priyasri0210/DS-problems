#efficiently handling the code. I don't wanna waste a function name, definition
def square(val):
    return val**2

print(square(5))
print(square(10))

#anonymous functions - it won't have name, it will be in single line

#<name> = lambda argument : argument(operation)
square_lambda = lambda a : a**2
print(square_lambda(3))

sum_lambda = lambda a,b : a+b
sum = sum_lambda(2,4)
print(sum_lambda(2,4))