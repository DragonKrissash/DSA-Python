class Node:
    def __init__(self,data=0,lNode=None,rNode=None):
        self.data=data
        self.lNode=lNode
        self.rNode=rNode

class BinaryTree:

    def __init__(self):
        self.no_of_nodes=0
        self.root=None

    def isEmpty(self):
        return self.no_of_nodes==0

    def append(self,data):
        node=Node(data)
        if self.isEmpty():
            self.root=node
        else:
            parent=self.root
            child=self.root
            while child is not None:
                if child.data<data:
                    parent=child
                    child=child.rNode
                elif child.data>data:
                    parent=child
                    child=child.rNode
                else:
                    pass
            if parent.lNode is None and parent.rNode is not None:
                parent.lNode=node
            elif parent.rNode is None and parent.lNode is not None:
                parent.rNode=node
            elif parent.rNode is None and parent.lNode is None:
                if parent.data<data:
                    parent.rNode=node
                elif parent.data>data:
                    parent.lNode=node
        self.no_of_nodes+=1

    def inOrderTrav(self,temp):
          if temp is None:
              return
          self.inOrderTrav(temp.lNode)
          print(f'{temp.data} ')
          self.inOrderTrav(temp.rNode)


    def inOrder(self):
        if self.isEmpty():
            print('Empty!')
        else:
            self.inOrderTrav(self.root)

b=BinaryTree()
b.append(5)
b.append(3)
b.append(7)
b.append(2)
b.append(4)
b.append(6)
b.append(8)
b.inOrder()
print('root node data: ',b.root.data)
