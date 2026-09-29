class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None]*size
        self.front = -1
        self.rear = -1
    def enqueue(self, item):
        if self.rear == self.size - 1:
            print("Queue overflow")
            return
        if self.front == -1 and self.rear == -1:
            self.front = self.rear = 0
            self.queue[self.rear] = item
            print(f"{item} is inserted into queue")
            return
        self.rear += 1
        self.queue[self.rear] = item
        print(f"{item} is inserted")
        return
    def dequeue(self):
        if self.front == -1:
            print("queue over flow")
            return
        item = self.queue[self.front]
        self.front += 1
        if self.front > self.rear:
            self.front = self.rear = -1
        print(f"{item} deleted from the queue")
        return
    def peek(self):
        if self.front == -1:
            print("the queue is empty")
            return
        item = self.queue[self.front]
        print(f"the front element is {item}")
        return
    def display(self):
        if self.front == -1:
            print("th4e queue is empty")
            return
        for i in range(self.front, self.rear+1):
            print(f"{self.queue[i]}", end=" | ")
        print("")
        return

def main():
    print("CSE25106, Ch. Jai ram charan.")
    queue = Queue(5)
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
            print("Exiting the program")
            break
        else:
            print("Invalid choice")
        
if __name__ == '__main__':
    main()
        