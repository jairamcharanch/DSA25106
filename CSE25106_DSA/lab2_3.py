#Binary search of unsorted array.
arr = []
n = int(input("Enter no of elements:"))
for i in range(n):
    element = int(input("Enter the element:"))
    arr.append(element)
# To check and sort the list.
if arr == sorted(arr):
    print("\n The input list is already sorted")
else:
    print("\nThe input list is not sorted")
    print("\nSorting the list....")
    arr.sort()
print("\nThe sorted list is:",arr)
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
    print("Element found at index:",result)
else: 
    print("Element not found")
    