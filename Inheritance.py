# Single Inheritance
print("\nSingle Inheritance")
class Parent:
    def pout(self):
        print(f"Hello I am Parent")

class Child(Parent):
    def cout(self):
        print(f"Hello I am Child")

c=Child()
c.cout()
c.pout()

# Multilevel Inheritance
print("\n\nMultilevel Inheritance")
class GrandParent:
    def gout(self):
        print(f"Hello I am GrandParent")

class Parent(GrandParent):
    def pout(self):
        print(f"Hello I am Parent")

class Child(Parent):
    def cout(self):
        print(f"Hello I am Child")

c=Child()
c.cout()
c.pout()
c.gout()




# Multiple Inheritance
print("\n\nMultiple Inheritance")
class Father:
    def fout(self):
        print(f"Hello I am Father")

class Mother:
    def mout(self):
        print(f"Hello I am Mother")

class Child(Father,Mother):
    def cout(self):
        print(f"Hello I am Child")

c=Child()
c.cout()
c.fout()
c.mout()



# Heirarchial Inheritance
print("\n\nHeirarchial Inheritance")
class Parent:
    def pout(self):
        print(f"Hello I am Parent")

class Brother(Parent):
    def bout(self):
        print(f"Hello I am Brother")

class Sister(Parent):
    def sout(self):
        print(f"Hello I am Sister")

b=Brother()
b.bout()
b.pout()

s=Sister()
s.sout()
s.pout()


# Hybrid Inheritance
print("\n\nHybrid Inheritance")
class GrandParent:
    def gpout(self):
        print(f"Hello I am GrandParent")


class Son(GrandParent):
    def sout(self):
        print(f"Hello I am Son")


class DaughterInLaw:
    def dout(self):
        print(f"Hello I am Daughter in Law")

class GrandSon(Son,DaughterInLaw):
    def gsout(self):
        print("Hello I am Grand Son")

gs=GrandSon()
gs.gpout()
gs.sout()
gs.dout()
gs.gsout()


#     GrandParent
#      /      
#    Son      DaughterInLaw
#      \      /
#      GrandSon