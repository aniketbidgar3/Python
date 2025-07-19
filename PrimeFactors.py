n=int(input("Enter Number : "))

def isPrime(n):
    for i in range(2,n):
        if(n%i==0):
            return 0
    return 1

for i in range(2,n):
    if(n%i==0):
        if(isPrime(i)):
            print(i,end=" ")
