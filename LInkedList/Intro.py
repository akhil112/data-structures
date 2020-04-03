
class Node:

    def __init__(self,data):
        self.data = data
        self.nextNode = None


class LinedList(object):

    def __init__(self):
        self.head = None

    def insertAtStart(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode



    def insertAtEnd(self, data):

        if self.head is None:
            print("Node is empty")
            return
        else:
            actualNode = self.head
            newNode = Node(data)
            while actualNode.nextNode is not None:
                actualNode = actualNode.nextNode
            actualNode.nextNode  = newNode
            newNode.nextNode = None

    def size(self):
        actualNode = self.head
        size = 0
        while actualNode is not None:
            size += 1
            actualNode = actualNode.nextNode
        return size

    def traverse(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        else:
            actualNode = self.head
            while  actualNode is not None:
                print(actualNode.data)
                actualNode = actualNode.nextNode

    def remove(self,data):
        if self.head is None:
            print("Linkedlist is empty")
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


israel = LinedList()
israel.insertAtStart(1)
israel.insertAtStart(2)
israel.insertAtStart(3)
israel.insertAtStart(4)
israel.insertAtEnd(5)
print("The size of linkedinlist is {} ".format(israel.size()))
israel.traverse()

israel.remove(4)
print("The size of linkedinlist is {} ".format(israel.size()))
israel.traverse()

