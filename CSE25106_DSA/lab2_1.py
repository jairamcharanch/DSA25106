# Linear search
arr=[]
n = int(input("Enter no of elements:"))
for i in range(n):
    elements = int(input("Enter the elements:"))
    arr.append(elements)
key = int(input("Enter element to search:"))
def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
        else:
            i+= 1
    return -1

result = linear_search(arr,key)
if result != -1 :
    print("Element found at index ",result)
else: 
    print("Element not found")