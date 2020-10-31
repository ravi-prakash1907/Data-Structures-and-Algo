## Write a python program to find the Largest Two Numbers in a given Array

import numpy as np

temp = []
size = int(input("Size of array: "))
print("Enter", size," elements!")

for i in range (0,size):
    temp.append(int(input("")))

# taking the unique elements
arr = np.array(list(dict.fromkeys(temp)))

if np.size(arr) >= 2:
    arr = np.sort(arr)
    print("Largest 2 numbers in array: \n", arr[-1]," & ",arr[-2])
elif np.size(arr) == 1:
    print("Array has only one unique element: ",arr[-1])





