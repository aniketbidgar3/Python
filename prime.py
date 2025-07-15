import math as m

def prime(n):
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