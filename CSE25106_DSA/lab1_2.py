#Growth 
n = int(input("Enter number of years:"))
p = int(input("Enter annual principal:"))
def growth(p,n):
    if n <= 0:
        return 1
    else:
        return p*growth(p,n-1)
    
print(growth(p,n))
    