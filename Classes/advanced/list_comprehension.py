a = [1,2,3,4,5,7,9,10]
sq_a = []
for i in a:
    if i >= 5:
        continue
    i = i**2
    sq_a.append(i)
print(sq_a)

#List comprehension
#output will be always list
#variable_name = [expression for <variable> in <list,tuple,dic,set>]
# sq_a = [i**2 for i in a]
# print(sq_a)


#variable_name = [<variable>(expression) for <variable> in <list,tuple,dic,set> if condition]
# sq_a = [i**2 for i in a if i<5]
# print(sq_a)

# fruits_lis = [6,4,3]
fruits = {"banana":5,
          "Mango":3,
          "Apple":2}

fruits_lis = [val+1 for key,val in fruits.items()]
print(fruits_lis)

fruits_lis = [fruits[i]+1 for i in fruits]
print(fruits_lis)




