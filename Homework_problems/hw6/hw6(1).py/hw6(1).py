import math
num = int(input("Enter a number: "))
#print(f"The square root of {num} is: {math.sqrt(num)}")

if num >= 0:
    print(f"The factorial of {num} is: {math.factorial(num)}")
    print(f"The square root of {num} is: {math.sqrt(num)}")

else:
    print(" Not defined for negative numbers.")
