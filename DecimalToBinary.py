dn = int(input("Enter Decimal Number : "))
pow = 1
bn = 0
while (dn != 0):
    digit = dn % 2
    bn = bn+digit*pow
    pow *= 10
    dn = int(dn/2)


print("Binary Number is :", bn)
