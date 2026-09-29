class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None]*size
        self.front = -1
        self.rear = -1
    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("queue over flow")
            return
        if self.front == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = item
            print(f"{item} inserted")
            return
        self.rear = (self.rear+1) % self.size
        self.queue[self.rear] = item
        print(f"{item} inserted")
        return
    def dequeue(self):
        if self.front == -1:
            print("queue under flow")
            return
        item = self.queue[self.front]  
        self.front = (self.front+1) % self.size
        if self.front == (self.rear+1) % self.size:
            self.front = self.rear = -1
        print(f"{item} deleted")
        return
    def peek(self):
        if self.front == -1:
            print("the queue is empty")
            return
        item = self.queue[self.front]
        print(f"{item} is the font element")
        return
    def display(self):
        if self.front == -1:
            print("the queue is empty")
            return
        i = self.front
        while i != (self.rear + 1)%self.size:  
            print(self.queue[i], end="|")
            i = (i+1) % self.size
        print("")
        return
        
def main():
    print("CSE25106, Ch. Jai ram charan.")
    queue = CircularQueue(5)
    while True:
        print("1.Enqueue\n2.Dequeue\n3.Peek\n4.Display\n5.Exit")
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            queue.enqueue(int(input("Enter the item: ")))
        elif choice == 2:
            queue.dequeue()
        elif choice == 3:
            queue.peek()
        elif choice == 4:
            queue.display()
        elif choice == 5:
            print("Exiting the program.....")
            break
        else:
            print("Invalid choice")
        
if __name__ == '__main__':
    main()            