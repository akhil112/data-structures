class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None


class LL:
    def __init__(self):
        self.head = None

    def insertAtStart(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def traversal(self):
        if self.head is None:
            print("LinkedList is empty")
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

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next = current.nextNode
            current.nextNode = prev
            prev = current
            current = next
        self.head   = prev

    def remove_duplicates(self):

        if self.head is None:
            print("Head is empty")

        else:
            actualNode = self.head
            prev = None
            dic = {}
            while actualNode is not None:
                temp = actualNode.data

                if temp in dic:

                    prev.nextNode = actualNode.nextNode
                    actualNode = None

                else:
                    dic[temp] = 1
                    prev = actualNode
                actualNode = prev.nextNode









akhil = LL()
akhil.insertAtStart(0)
akhil.insertAtEnd(1)
akhil.insertAtEnd(2)
akhil.insertAtEnd(3)
akhil.insertAtEnd(4)
akhil.insertAtEnd(2)
print("Before reversal ")
akhil.traversal()

print("After reversal")
akhil.reverse()
akhil.traversal()

print("After removing duplicates")
akhil.remove_duplicates()
akhil.traversal()


