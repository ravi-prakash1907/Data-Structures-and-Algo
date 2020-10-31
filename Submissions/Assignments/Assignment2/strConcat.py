## Write a python program to concatenate two strings.

def concat(s1, s2):
    return s1+s2

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

joined = concat(str1, str2)
print("Concatinated string: ",joined)
