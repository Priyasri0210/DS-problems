#Data Structure - how we store the store in memory
#List , Tuples , Dictionary and Set

#syntax
a = []
a = [1,2,3,4,5,6,7,8,1,23,4,5,6,7]
a = [1.4,21.7,10.0]
a = ['bha','ta','bhb']
a = [1, 12.7, 'bha']
print(type(a))

#List is mutable (altering the list)
a = [1,2,3,4]
a.append(6)
print(a)

a.remove(1) #Removes the value in list
print(a)
a.pop(3) #Removes last value #removes based on index
print(a)

#List is ordered(It will be in same order all time)
a = [1,2,3,4,5]
a.append(6)
print(a)

#use index to get the values
print(a[3])
print(a[1])
a[2] = 10
print(a)

#for <variable> in <list varaible>:
for i in a:
    print(i)



