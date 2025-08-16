class queue:
    def __init__(self):
        self.arr = []

    def isEmpty(self):
        return len(self.arr) == 0

    def enque(self, val):
        self.arr.append(val)

    def deque(self):
        if (self.isEmpty()):
            print("Queue is Empty")
        else:
            self.arr.pop(0)

    def peek(self):
        if (self.isEmpty()):
            return ("Queue is Empty")
        else:
            return self.arr[0]

    def out(self):
        print(self.arr)


q = queue()

q.out()

q.enque(12)
q.enque(18)
q.enque(17)

q.out()

print(q.peek())

q.deque()

q.out()

print(q.peek())
