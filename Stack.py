
class stack:
    def __init__(self):
        self.arr = []

    def isEmpty(self):
        return (len(self.arr) == 0)

    def push(self, val):
        self.arr.append(val)

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            self.arr.pop()

    def top(self):
        if self.isEmpty():
            return ("Stack is Empty")
        else:
            return self.arr[-1]

    def out(self):
        print(self.arr)


s = stack()

print(s.isEmpty())

s.push(22)
s.push(58)
s.push(19)

s.out()

s.pop()

s.out()

print(s.top())

print(s.isEmpty())
