
# Public : All members are by default Public (Access : Everywhere)
# Private : '__' is used to declare private members (Access : Inside Class Only)
# Protected : '_' is used to declare Protected members (Access : For Inheritance )

class Base:
    def __init__(self,name,age):
        self.__name=name
        self._age=age

    def __str__(self):
        return (f"Hello I am {self.__name}, {self._age} years old")



b=Base("Aniket",22)
b.__name="Akshada" #Trying to change private Member but it is not possible
b._Base__name="Akshada" #Trying to change private Member but it is possible here when we use Base class to Access
b._age=18 #Trying to change protected member it is possible
print(b)
