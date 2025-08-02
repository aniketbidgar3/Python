# Static Method is Method That Dont Have  Self Parameter

# we use @staticmethod Decorator to run this method

class Parent:
    def __init__(self):
        print("I am Constructor")

    @staticmethod
    def hello(name):
        print("Hello", name)


p1 = Parent()
p1.hello("Aniket")


# To run Static Method without @staticmethod Decorator


class Parent:
    @staticmethod
    def __init__():
        print("I am Constructor")

    def hello(name):
        print("Hello", name)


p1 = Parent()
Parent.hello("Ankita")
