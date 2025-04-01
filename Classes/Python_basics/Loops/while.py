#while and for
#while

#syntax
#while <condition>(True or False):
#    logics

#should be careful while creating while loop
#It should have some condition at which the while false
#1 . Condition at which it fails
#2. Use break 

#Conditional method to break the loop
count = 10
while count <= 10 and count != 0:
    print(count)
    count = count - 1
print("Done")

#Using break
count = 0
while True:
    print(count)
    count = count + 1
    if count == 10:
        break
print("Done")


#Other keywords
#continue(it skips)
count = 0
while True:
    if count == 5:
        count = count + 1
        continue
    print(count)
    count = count + 1
    if count == 10:
        break
print("Done")