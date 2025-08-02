class GrandParent:

    def out(self):
        print("I am GrandParent")


class Parent(GrandParent):
    # pass
    def out(self):
        print("I am Parent")


class Child(Parent):
    # pass
    def out(self):
        print("I am Child")


c = Child()
c.out()

p = Parent()
p.out()

g = GrandParent()
g.out()
