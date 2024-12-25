#  Write a Python program that takes a positive integer input from the user and calculates its factorial. 

# number = int(input("Enter a number: "))
# fac = 1
# i = 1
# while i <= number :
#     fac *= i
#     i += 1
# print(f"The factorial of {number} is {fac}.")

number = int(input("Enter a positief integer: "))
if number <= 0 :
    print("Factorial is defined with positief numbers only.")
else :
    fac = 1
    for i in range(1,number+1) :
        fac *= i
    print(f"The factorial of {number} is {fac}.")

