print("Implementation of DLL")

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
    # Creation
    def create(self):
        n = int(input("Enter no of elements: "))
        for i in range(n):
            data = int(input("Enter the values: "))
            new = Node(data)
            if self.head is None:
                self.head = new
            else:
                temp = self.head
                while temp.next:
                    temp = temp.next
                temp.next = new
                new.prev = temp

    # Insert begin
    def insert_begin(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new

    # Insert end
    def insert_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
            new.prev = temp

    # Insert at specific index
    def insert_index(self, index, data):
        if index < 0:
            print("Invalid index")
            return
        if index == 0:
            self.insert_begin(data)
            return
        if self.head is None:
            print("Invalid index")
            return
        temp = self.head
        for i in range(index - 1):
            if temp.next is None:
                print("Invalid index")
                return
            temp = temp.next
        new = Node(data)
        new.next = temp.next
        new.prev = temp
        if temp.next is not None:
            temp.next.prev = new
        temp.next = new

    # Delete specific value
    def delete(self, data):
        if self.head is None:
            print("No data")
            return
        temp = self.head
        while temp and temp.data != data:
            temp = temp.next
        if temp is None:
            print("Value not present")
        else:
            if temp.prev is not None:
                temp.prev.next = temp.next
            else:
                self.head = temp.next
            if temp.next is not None:
                temp.next.prev = temp.prev
            print("Value deleted")

    # Delete begin
    def delete_begin(self):
        if self.head is None:
            print("No data to delete")
        else:
            temp = self.head
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            print("Deleted value = ", temp.data)

    # Delete end
    def delete_end(self):
        if self.head is None:
            print("No data to delete")
        elif self.head.next is None:
            print("Deleted value = ", self.head.data)
            self.head = None

        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            print("Deleted value = ", temp.data)
            temp.prev.next = None

    # Count
    def count(self):
        if self.head is None:
            print("No data to count")
        else:
            count = 0
            temp = self.head
            while temp:
                count += 1
                temp = temp.next
            print(f"Number of nodes = {count}")

    # Display / Traverse
    def display(self):
        if self.head is None:
            print("No data")
        else:
            temp = self.head
            while temp:
                print(temp.data, end=" <--> ")
                temp = temp.next

            print("None")


DLL = DoubleLinkedList()

while True:
    print("\n1.Create DLL")
    print("2.Insert at beginning")
    print("3.Insert at ending")
    print("4.Insert at index")
    print("5.Delete by value")
    print("6.Delete first node")
    print("7.Delete last node")
    print("8.Count no of nodes")
    print("9.Display / Traverse")
    print("10.Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        DLL.create()
        print("DLL is created")

    elif choice == 2:
        data = int(input("Enter data to insert: "))
        DLL.insert_begin(data)
        print("Data is inserted at beginning")

    elif choice == 3:
        data = int(input("Enter data to insert: "))
        DLL.insert_end(data)
        print("Data is inserted at ending")

    elif choice == 4:
        data = int(input("Enter data to insert: "))
        index = int(input("Enter the index: "))
        DLL.insert_index(index, data)

    elif choice == 5:
        data = int(input("Enter data to delete: "))
        DLL.delete(data)

    elif choice == 6:
        DLL.delete_begin()

    elif choice == 7:
        DLL.delete_end()

    elif choice == 8:
        DLL.count()

    elif choice == 9:
        DLL.display()

    elif choice == 10:
        print("Exiting the program")
        break

    else:
        print("Invalid choice")