#Exceptions - issues created during run time
# try except



#try - should have all the logics and code
#exception should have code to handle the issue
#finally - it gets executed even in try and even in exception

#try:
    #all the codes
#except Exception as <variable_name>:
    #print(<varaible_name>)
#finally:
    #code to get execute

#Specific exception(zero division)
try:
    a = 10
    b = 0
    print(a/b)
except ZeroDivisionError:
    print("Can't divide by zero")
finally:
    print('Done')


#generic exception
try:
    a = 'abc'
    print(int(a)) 
except Exception as e:
    print(e)
print('Done')

try:
    a = 10
    print(a/0) 
except Exception as e:
    print(e)
print('Done')


