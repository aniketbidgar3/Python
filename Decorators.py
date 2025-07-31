def greet(fx):
    def myfunc():
        print("Hello I am Here to Serve You !")
        fx()
        print("Thank You for Using Me !")
    return myfunc

@greet
def hello():
    print("Hello World")


@greet
def add():
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    print(f"Sum is {a+b}")


add()



# hello()

# Another Technique to call this function

# greet(hello)()