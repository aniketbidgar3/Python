n=int(input("Enter Any Number : "))

sum=1
for i in range(2,n):
    if(n%i==0): 
        sum+=i


if(sum==n):
    print("This is Perfect Number")
else:
    print("This is Not Perfect Number")


# Some Perfect Numbers are
# 6 28 496 8128