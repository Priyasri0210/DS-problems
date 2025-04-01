a = ()
print(type(a))

#Tuple is not mutable(altering is not possible)
#Tuple is also ordered

a = (1,2,3,4,5)
s = list(a)
se = set(a)

print(s)
print(se)
print(a[3])

for i in a:
    print(i)
