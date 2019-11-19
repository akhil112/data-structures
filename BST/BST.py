class Node():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


class BST():

    def __init__(self):
        self.root = None

    
        
    
    def insert1(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert(data,self.root)
    
    def insert(self,data,cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self.insert(data,cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self.insert(data,cur_node.right)
                
        else:
            print("duplicates are not allowed in BST")
    
    def traverse(self):
        pass
            
            
p = BST()
p.insert1(4)
p.insert1(1)
p.insert1(3)