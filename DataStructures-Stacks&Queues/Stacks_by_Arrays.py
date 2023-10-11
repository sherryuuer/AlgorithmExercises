class Stack:
    def __init__(self):
        self.array = []
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def peak(self):
        if self.array:
            print(self.array[-1])

    def push(self, data):
        self.array.append(data)
        print(self.array)
        self.length += 1

    def pop(self):
        data = self.array.pop()
        print(data)
        print(self.array)
        self.length -= 1


mystack = Stack()
mystack.push(4)
mystack.push(5)
mystack.push(6)
mystack.peak()
mystack.pop()
print(mystack)
