#Count Down
def countdown(n):
    if n >= 0 :
        if n != 0:
            print(n) 
            return countdown(n-1)
        else:
            print("Launch!")
        
n= int(input("Enter the number:"))
countdown(n)
