# code to append in file

f = open("alvira.txt", "a")

f.write("Hello I am Alvira\n")
f.write("I am 20 Years Old\n")


# code to write in file

data=input("Enter data : ")

while(data!="stop"):
    f.write("\n")
    f.write(data)
    data=input("Enter data : ")

f.close()


# code to read whole file

f=open("alvira.txt","r")

data=f.read()

print(data)

f.close()
