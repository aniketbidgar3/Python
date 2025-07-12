class Student:
    def __init__(self,rollNo,name,age,percentage):
        self.rollNo=rollNo
        self.name=name
        self.age=age
        self.percentage=percentage

    def __str__(self):
        return (f"Hello my name is {self.name} \nRoll No : {self.rollNo}\nAge : {self.age}\nPercentage : {self.percentage} ")
    
    def printBranch(self):
        print(f"My branch is {self.branch} and my favorite subject is {self.fSubject}")
    
class CompStudent(Student):
   
    branch="Computer"
    fSubject="DSA"
    
  
class MechStudent(Student):
   
    branch="Mechanical"
    fSubject="Math"
    
    


s=CompStudent(26,"Aniket Bidgar",22,85.80)
print(s)
s.printBranch()