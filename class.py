class Student:
    def __init__(self, rollNo, name, age, percentage):
        self.rollNo = rollNo
        self.__name = name
        self.age = age
        self.percentage = percentage

    def setName(self,name):
        self.__name=name

    def __str__(self):
        return (f"Hello my name is {self.__name} \nRoll No : {self.rollNo}\nAge : {self.age}\nPercentage : {self.percentage} ")


s = Student(26, "Aniket Bidgar", 22, 85.80)
# s.__name="Alvira"
# s.setName("Alvira")
print(s)


# public private protected