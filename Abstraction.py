class Parent:
    def __init__(self, name):
        self.__name = name

    def __hello(self):
        print("Hello", self.__name)

    def welcome(self):
        self.__hello()


p = Parent("Aniket")
p.__hello()
p.welcome()


# I have to Edit it
