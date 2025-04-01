#Dynamic
a = input("Enter the value 1")
b = input("Enter the value 2")

#Type conversion
#if the string value is digits
#string ---> int 
#string ---> float

#string ---> int/float (not possible if it is not a digit)

#int --> string
#float ---> string

#int --> float
#float --> int (Not possible)

print(type(a))
a = int(a)
b = int(b)
print(type(a))


#Addition
c = a + b
# string + string --> possible
# bharath + kumar ---? bharathkumar

# int + int --> possible
# 1 + 2 --> 3

# string + int ---> not possible
# string + str(int) ---> possible
# string + string

print("The Addition value is " + str(c))
# print(a+b)

#SUbtraction
print(a-b)

#Multiply
print(a*b)

#Division
print(a/b)


#Formatting string
print("The Addition value is {0}, input 1 is {1}, input 2 is {2}".format(c,a,b))

