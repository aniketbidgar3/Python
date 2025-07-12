class Student:
    def __init__(self,rollNo,name,age,percentage):
        self.rollNo=rollNo
        self.name=name
        self.age=age
        self.percentage=percentage

    def __str__(self):
        return (f"Hello my name is {self.name} \nRoll No : {self.rollNo}\nAge : {self.age}\nPercentage : {self.percentage} ")
    
    
s=Student(26,"Aniket Bidgar",22,85.80)
print(s)