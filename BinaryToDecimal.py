bn=int(input("Enter binary Number : "))
pow=1
dn=0
while(bn!=0):
    digit=bn%10
    dn=dn+digit*pow
    pow*=2
    bn=int(bn/10)


print("Decimal Number is :",dn)
