a = int(input("enter a number "))
r = 0
while a>0:
    digit = a % 10
    r = r*10 + digit
    a=a//10

print(r)
