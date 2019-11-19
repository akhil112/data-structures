class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None
        
        

class LinkedList:
    def __init__(self):
        self.head = None
        self.store = []
        
    
    
        
    def traverse(self):
        if self.head is None:
            print("list is empty")
            return
        else:
            actualNode = self.head
            while actualNode is not None:
                print(actualNode.data)
                # self.store.append(actualNode.data)
                actualNode = actualNode.nextNode
            
    
    def insertAtStart(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        
        else:
            newNode.nextNode = self.head
            self.head = newNode
    
    
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
            
    
    def removingDuplicates(self):
        actualNode = self.head
        previousNode = None
        
        while actualNode is not None:
            
            previousNode = actualNode
            actualNode = actualNode.nextNode
            if actualNode.data  not in self.store:
                self.store.append(actualNode.data)
                
            else:
                previousNode.nextNode = actualNode.nextNode
                  
            
            
        
            
CLL = LinkedList()
CLL.insertAtStart(1)
CLL.insertAtStart(2)
CLL.insertAtStart(3)
CLL.insertAtEnd(4)
CLL.insertAtEnd(1)
CLL.traverse()

print("After removing duplicates")
CLL.removingDuplicates()
CLL.traverse()
            

            
            
            
            