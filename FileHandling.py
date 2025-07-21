# code to append in file

f=open("file.txt","a")


# code to write in file

# data=input("Enter data : ")

# while(data!="stop"):
#     f.write("\n")
#     f.write(data)
#     data=input("Enter data : ")

# f.close()


# code to read whole file 

# f=open("file.txt","r")

# data=f.read()

# print(data)

# f.close()


# code to read file line by line

f=open("file.txt","r")

for line in f:
    print(line)

f.close()