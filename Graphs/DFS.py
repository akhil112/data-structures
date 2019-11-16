class Node(object):
    def __init__(self,name):
        self.name = name
        self.adjacenciestList = []
        self.visited = False

class DFS(object):

    def dfs(self,node):

        node.visited = True
        print(node.name)

        for i in node.adjacenciestList:
            if not i.visited:
                self.dfs(i)



node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")
node5 = Node("E")


node1.adjacenciestList.append(node2)
node1.adjacenciestList.append(node3)
node2.adjacenciestList.append(node4)
node1.adjacenciestList.append(node5)


akhil = DFS()
akhil.dfs(node1)