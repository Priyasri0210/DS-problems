a = ['bharath','kumar',25,'Male']

#{"key":"value"}

a = {}
#Contacts
a = {"Firstname" : "Bharath",
     "Middlename": "Kumar",
     "Age":25,
     "Gender":"Male"}
#syntax
#{"key":"value","key":"value"}

#The keys should be unique
#nested dictionaries

# a = {
#     "name":
#             {
#             "firstname":"Bharath",
#             "Middlename":"Kumar"
#             }
#     }

for key,value in a.items():
    print(key , str(value))

for i in a:
    #dictionary_variable[already_present_key]
    print(a[i])


#Insert
#dictionary_variable['new_key'] = 'value'
a['Lastname'] = 'Kalaimani'
print(a)
#del dictionary_variable[already_present_key]
del a['Firstname']
a['Firstname'] = ''
# del a
print(a)

#Dictionary is also mutable
#Dictionary is also ordered
#Keys should be unique