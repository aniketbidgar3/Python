# Prime Number Using For Else Loop

n = int(input("Enter Number : "))


if (n < 0):
    raise Exception("Prime Numbers Must be Positive")

for i in range(2, int(n/2)):
    if (n % i == 0):
        print("Number is Not Prime")
        break
else:
    print("Number is  Prime")
