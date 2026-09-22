class Queue:
    def __init__(self,size):
        self.size = size
        self.queue = [None]*size
        self.front = -1
        self.rear = -1
    
    def enqueue(self,x):
        if self.rear == size - 1 :
            print("Queue Overflow")
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.queue[self.rear] = x
            print(f"{x} inserted into queue")
    
    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            print("Queue Underflow")
        else:
            x = self.queue[self.front]
            self.queue[self.front] = None
            self.front += 1
            print(f"{x} deleted from queue")
            if self.front > self.rear:
                self.front = -1
                self.rear = -1
                
    def peek(self):
        if self.front == -1:
            print("Queue empty")
        else:
            print("First element in queue is ",self.queue[self.front])
    
    def display(self):
        if self.front == -1:
            print("Queue empty")
        else:
            while self.front <= self.rear:
                temp = self.front
                print("Queue:",self.queue[temp])
                self.front += 1 
                
print("Queue using Array:")
size = int(input("Enter the size:"))
q = Queue(size)
while True:
    print("1.Enqueue")
    print("2.Dequeue")
    print("3.Peek")
    print("4.Display")
    print("5.Exit")
    
    choice = int(input("Enter your choice between(1-5):"))
          
    if choice == 1:
        x = int(input("Enter element to insert:"))
        q.enqueue(x)
    elif choice == 2:
        q.dequeue()
    elif choice == 3:
        q.peek()
    elif choice == 4:
        q.display()
    elif choice == 5:
        print("Exiting program")
        break
    else:
        print("Invalid choice")
        
        