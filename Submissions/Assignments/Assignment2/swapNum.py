## Write a python program to swap two numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("\nBefore Swapping: ")
print("num1 = ",num1,"  num2 = ",num2)

# swapping
num1 += num2
num2 = num1 - num2
num1 -= num2

print("\nAfter Swapping: ")
print("num1 = ",num1,"  num2 = ",num2)
