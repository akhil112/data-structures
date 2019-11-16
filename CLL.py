class  Node():

    def __init__(self,data):
        self.data = data
        self.next = None


class CLL():

    def __init__(self):
        self.head  = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def prepend(self,data):

        newNode = Node(data)
        start = self.head
        self.head = newNode
        newNode.next = start


    def traversal(self):
        cur = self.head

        while cur:
            print(cur.data)
            cur = cur.next
            if cur==self.head:
                break






akhil = CLL()
akhil.append(1)
akhil.append(2)
akhil.prepend(0)

akhil.traversal()