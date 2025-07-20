
def prime(n):
    '''
    This Function Prints Only Prime Numbers.
    But Here I used To Print All Prime Numbers In a Range
    '''
    flag=1
    for i in range(2,int(n/2)):
        if(n%i==0):
            flag=0
            break
    
    if(flag==1):
        print(n,end=" ")
    


n=int(input("Enter Number : "))

for i in range(2,n+1):
    prime(i)

print(prime.__doc__)
