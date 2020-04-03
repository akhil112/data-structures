class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        val = self.queue[0]
        del self.queue[0]
        return val

    def size(self):
        return len(self.queue)

    def peek(self):
        return self.queue[0]


akhil = Queue()
akhil.enqueue(1)
akhil.enqueue(2)
akhil.enqueue(3)
print("Size of queue is {}".format(akhil.size()))
print("removed element is {}".format(akhil.dequeue()))
print("Peek element is {}".format(akhil.peek()))
print("Size of queue is {}".format(akhil.size()))


