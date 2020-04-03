class Stack:

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        temp = self.stack[-1]
        del self.stack[-1]
        return temp

    def peek(self):
        return self.stack[-1]

    def sizestack(self):
        return len(self.stack)


akhil = Stack()
akhil.push(1)
akhil.push(2)
akhil.push(3)
print("size of stack is {}".format(akhil.sizestack()))
print("removed element is {}".format(akhil.pop()))
akhil.peek()
print("size of stack after removal {} ".format(akhil.sizestack()))