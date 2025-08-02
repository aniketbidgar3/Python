

# def prime(n):
#     flag=1
#     for i in range(2,n):
#         if(n%i==0):
#             flag=0
#             break

#     if(flag==1):
#         print(n,end=" ")


# n=int(input("Enter Number : "))
# if(n<2):
#     raise ValueError("Prime Number Should be start from 2 and Are Always Positive")


# for i in range(2,n+1):
#     prime(i)

salary = int(input("Enter Your Salary : "))

if (salary < 0):
    raise ValueError("Salary Should be greater than 0")

Tax = (5/100)*salary

print(f"Tax on Your Salary is : {Tax}")
