## Write a python program to swap two arrays.

def getData(size):
    arr = []
    for i in range (0,size):
        arr.append(input("Enter an element: "))
    return arr


len1 = int(input("Enter the size of first array: "))
arr1 = getData(len1)
len2 = int(input("Enter the size of second array: "))
arr2 = getData(len2)


print("\nBefore Swapping: ")
print("array-1 = ",arr1," | array-2 = ",arr2)

# swapping
temp = arr1
arr1 = arr2
arr2 = temp
del temp

print("\nAfter Swapping: ")
print("array-1 = ",arr1," | array-2 = ",arr2)