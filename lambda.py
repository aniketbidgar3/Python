square=lambda x : x*x

# def square(x):
#     return x*x

cube=lambda x:x**3

add=lambda a,b : a+b

sub=lambda a,b:a-b

mul=lambda a,b:a*b

div=lambda a,b:a/b

# def max(a,b):
#     if(a>b):
#         return a
#     else:
#         return b

max=lambda a,b:a if a>b else b

min=lambda a,b:a if a<b else b

evenOdd =lambda a:(f"{a} is Even") if a%2==0 else (f"{a} is Odd")



print("Square           : ",square(5))
print("Cube             : ",cube(5))
print("Addition         : ",add(12,12))
print("Substraction     : ",sub(12,12))
print("Multiplication   : ",mul(12,12))
print("Division         : ",div(12,12))
print("Minimum          : ",min(12,5))
print("Maximum          : ",max(12,5))
print(evenOdd(12))
print(evenOdd(5))
