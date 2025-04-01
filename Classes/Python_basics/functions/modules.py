#Modules --> using the function from different files or using from packages
#from <filename> import <function name>

#This is user defined
from function import calculator
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    oper = input()
    result = calculator(a,b,oper)
    print(result)


#user defined modules - importing functions which is already written by me
#inbuilt modules - Importing modules which is already present in python
#external modules

#
