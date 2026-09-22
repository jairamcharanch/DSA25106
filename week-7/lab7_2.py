class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,x):
        new = Node(x)
        if self.rear is None:
            self.front = self.rear = new
        else:
            self.rear.next = new
            self.rear = new
            print(f"{x} inserted in the queue.")
    
    def dequeue(self):
        if self.front == None:
            print