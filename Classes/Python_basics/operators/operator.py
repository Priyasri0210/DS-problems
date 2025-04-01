#Arithmetic operators
# + , -, *, / , //, %

a = 1
b = 2
c = a + b
print(c)
c = a - b
print(c)
c = a * b
print(c)
#Division
c = a / b
print(c)

#Floor division
c = a // b
print(c)

#Modulo 
c = a % b
print(c)


#assignment operators
# = , += , -=, *=, /=

a = 5
#The variable name to the left and right of equal to should be same
a = a + 1
a += 1

a = a - 2
a -= 2

a = a * 2
a *= 2

a = a / 2
a /= 2



#Comparison operator
# ==, >, <, >=, <=

a = 1
b = 2
print(a == b)
print(a > b)
print(a < b)

#Logical Operator
#and , or, not

a = 1
b = 2

#OR
print(a>b or a<b)
#More priority will be for True
# False,True,True --> True
# True,True,True ---> True
# True,False,False --> True

#AND
print(a>b and a<b)
#More priority will be for False
# False,True,True --> False
# True,True,True ---> True
# True,False,True --> False

#NOT
print(not True)
print(not False)
