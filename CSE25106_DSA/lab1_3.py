#Searching of element
list = []
t=int(input("Enter number of inputs:"))
for _ in range(t):
    n = int(input("Enter the ID:"))
    list.append(n)
ID = int(input("Enter ID to seach:"))
start = 0
def search(list,ID,start):
    if list[start] == ID:
        print(f"ID found at{start}")
    elif start == len(list):
        print("ID not found")
    else:
        return search(list,ID,start+1)


search(list,ID,start)