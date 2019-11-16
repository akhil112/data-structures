class Node:

    def __init__(self,data):
        self.data = data
        self.nextNode =None

class LinedList(object):

    def __init__(self):
        self.head = None

    def insertAtStart(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
           newNode.nextNode = self.head
           self.head = newNode


    def traverse(self):
        if self.head is None:
            print("list is empty")
            return

        else:
            actualNode = self.head
            while actualNode is not None:
                print(actualNode.data)
                actualNode = actualNode.nextNode


    def insertAtEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            print("list is empty")
            return

        else:
            actualNode = self.head
            while actualNode.nextNode is not None:
                actualNode = actualNode.nextNode

            newNode.nextNode = None
            actualNode.nextNode = newNode

    def remove(self,data):
        if self.head is None:
            print("list is empty")
            return

        else:
            currentNode = self.head
            previousNode = None
            while currentNode.data != data:
                previousNode = currentNode
                currentNode = currentNode.nextNode

            if previousNode is None:
                self.head = currentNode.nextNode

            else:
                previousNode.nextNode = currentNode.nextNode

    def size(self):
        size = 0
        actualNode = self.head

        if actualNode is None:
            print("list is empty")
            return

        else:

            while actualNode is not None:
                size += 1
                actualNode = actualNode.nextNode

            print(size)


LL = LinedList()
LL.insertAtStart(1)
LL.insertAtStart(2)
LL.insertAtStart(3)
LL.insertAtEnd(99)
LL.insertAtEnd(69)
#LL.size()
LL.traverse()

LL.remove(69)
LL.traverse()
