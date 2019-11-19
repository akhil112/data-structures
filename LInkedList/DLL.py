class Node:
    def __init__(self,data):
        self.data = data
        self.previousNode = None
        self.nextNode  = None
        
        
        
        
class DoubleLL:
    def __init__(self):
        self.head = None
        
        
        
        
    def insert_at_start(self,data):
        if self.head is None:
            newNode = Node(data)
            self.head  = newNode
            return 
        else:
            newNode = Node(data)
            newNode.nextNode = self.head
            self.head.previousNode = newNode
            self.head = newNode
    
    
    def insert_at_end(self,data):
        newNode = Node(data)
        actualNode = self.head
        if actualNode is None:
            self.head = newNode
            return 
        else:
            while actualNode.nextNode is not None:
                actualNode = actualNode.nextNode
            newNode.previousNode = actualNode
            actualNode.nextNode = newNode
            
           
           
    
    
    
    def traverse_list(self):
         actualNode = self.head
         while actualNode is not None:
             print(actualNode.data)
             actualNode = actualNode.nextNode
    
    def insert_after_item(self,data):
        pass
    
    
    
    def insert_before_item(self,data):
        pass
    
     
    def delete_at_start(self):
        pass
     
    def delete_at_end(self):
        pass
     
     
    def delete_element_by_value(self,data):
        pass
     
     
     
     
DLL = DoubleLL()
DLL.insert_at_start(1)
DLL.insert_at_start(2)
DLL.insert_at_start(3)
DLL.insert_at_end(99)
DLL.insert_at_end(66)
DLL.traverse_list()