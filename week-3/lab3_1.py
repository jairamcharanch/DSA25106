def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    num = int(input(f"Enter the {i+1} element: "))
    arr.append(num)
bubble_sort(arr)
print(arr)

