from collections import namedtuple,defaultdict

#Combination of dictionary and tuple

#Declaring
# Person = namedtuple("Person",["name",'age','city'])
# print(Person)

# p1 = Person(name='Bharath',age=25,city='Chennai')

# print(p1.name)
# print(p1.age)
# p1.name = 'Kumar'


fruits = defaultdict(int)
print(fruits)
# fruits = {"banana":5,
#           "Mango":3,
#           "Apple":2}

fruits['banana'] = fruits["banana"] + 1
print(fruits)
# fruits['guava'] = 1
# print(fruits)
fruits['guava'] = fruits['guava'] + 1
print(fruits)

fruits = {"banana":5,
          "Mango":3,
          "Apple":2}

fruits = defaultdict(int)
print(fruits)
fruits['banana'] = 10
print(fruits['banana'])
print(fruits['guava'])

fruits = defaultdict(str)
print(fruits)
fruits['banana'] = 10
print(fruits['banana'])
print(fruits['guava'])




