#arguments or parameters

#positional arugument
#it follows order
def sum(val1,val2,oper):
    if oper == '+':
        print(val1+val2)
    else:
        print('Not supported')

a = 10
b = 20
c = '+'
#no. of arguments in func call and definition should be same
sum(a,b,c)
#the order of assignment gets changed
sum(c,a,b)

# #Keyword arguments
#no. of arguments in func call and definition should be same
sum(val1=a,val2=b,oper=c)
sum(oper=c,val1=a,val2=b)

def sum_default(val1,val2,oper='+'):
    if oper == '+':
        print(val1+val2)
    else:
        print('Not supported')
# Default arguments
sum_default(a,b)
sum_default(a,b,'-')



#variable length arguments
def sum(*val):
    sum = 0
    for i in val:
        sum = sum + i
    print(sum)

sum(1,2,3)
sum(1,2,3,4,5,6,7,8,9)

#keyword_varaible
def sum(**val):
    sum = 0
    for i in val:
        sum = sum + i
    print(sum)

sum(val1=10,val2=20)
