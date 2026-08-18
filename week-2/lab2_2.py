# Binary search of sorted array
arr=[]
n = int(input("Enter no of elements:"))
for i in range(n):
    elements = int(input("Enter the elements in sorted order:"))
    arr.append(elements)
key = int(input("Enter element to search:"))
def binary_search(arr,key):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low+high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

result = binary_search(arr,key)
if result != -1 :
    print("Element found at index :",result)
else: 
    print("Element not found")