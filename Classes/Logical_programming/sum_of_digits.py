# input = 123, 557, 12383778
# 123 = 1 + 2 + 3 = 6
# 557 = 5 + 5 + 7 = 17

# a = 1234
# a = str(a)
# sum = 0
# for i in a:
#     sum += int(i)
# print(sum)

a = int(input('Enter the number : '))
sum_of_digits = 0
while a>0:
    digits = a%10
    sum_of_digits = sum_of_digits + digits
    a = a//10
print(sum_of_digits)
