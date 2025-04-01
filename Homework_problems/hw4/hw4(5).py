num = int(input("enter the no.of terms "))
n1 = 0
n2 = 1
#print(n1)
#print(n2)
if num <=0:
    print("please enter valid number")
else:
    print(n1)
    print(n2)    
    for i in range(2,num):
        sum = n1 + n2
        print(sum)
        n1=n2
        n2=sum
print("done")    
 
    
