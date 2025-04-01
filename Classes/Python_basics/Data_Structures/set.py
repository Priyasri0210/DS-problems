#Set is mutable (alterations is possible)
#Set doesn't allow duplicates
#Set is unordered
# a = {1,2,3,4}
# print(a)

# #Inserting
# a.add(5)
# print(a)

# a.add(5)
# print(a)

# #removing(delete the values)
# a.remove(5)
# print(a)

# #shows error while the element is not present
# # a.remove(6)
# # print(a)

# #Not shows any error while the element is not present
# a.discard(6)
# print(a)

# a.discard(1)
# print(a)

# a.pop()
# print(a)

# a.pop()
# print(a)

# #I can use it for removing duplicates
a = [1,2,4,5,8,1,2]
s = set(a)
print(s)

#Union operation
lis_1 = [1,2,3,4,5]
lis_2 = [5,6,7,8,9]
set_1 = set(lis_1)
set_2 = set(lis_2)
print(set_1.union(set_2))

print(set_1.intersection(set_2))

print(set_1.difference(set_2))
print(set_2.difference(set_1))


#Set is mutable
#Set don't allow duplicates
#Set is unordered and its doesn't have index

#Python data structures
# List ---> Mutable, ordered, indexing
# Tuple ---> immutable, ordered, indexing
# Dictionary --> Mutable, ordered, index(key)
# Set --> Mutable, unordered, doesn't support index, unique


