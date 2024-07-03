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
        prev=None
        cur=self.root
        appended=False
        while not appended:
            if cur==None:
                if prev==None:
                    self.root=node
                    appended=True
                elif prev.data < data:
                    prev.rNode=node
                    appended=True
                elif prev.data > data:
                    prev.lNode=node
                    appended=True
            elif cur.data>data:
                prev=cur
                cur=cur.lNode
            elif cur.data<data:
                prev=cur
                cur=cur.rNode
        self.no_of_nodes+=1

    def inOrderTrav(self,temp):
          if temp is None:
              return
          self.inOrderTrav(temp.lNode)
          print(f'{temp.data} ',end=' ')
          self.inOrderTrav(temp.rNode)

    def preOrderTrav(self,temp):
        if temp is None:
            return
        print(f'{temp.data} ',end=' ')
        self.preOrderTrav(temp.lNode)
        self.preOrderTrav(temp.rNode)

    def posOrderTrav(self,temp):
        if temp is None:
            return
        self.posOrderTrav(temp.lNode)
        self.preOrderTrav(temp.rNode)
        print(f'{temp.data} ',end=' ')

    def inOrder(self):
        if self.isEmpty():
            print('Empty!')
        else:
            self.inOrderTrav(self.root)
            print('')

    def preOrder(self):
        if self.isEmpty():
            print('Empty!')
        else:
            self.preOrderTrav(self.root)
            print('')

    def posOrder(self):
        if self.isEmpty():
            print('Empty!')
        else:
            self.posOrderTrav(self.root)
            print('')


b=BinaryTree()
b.append(5)
b.append(25)
b.append(1)
b.append(12)
b.append(3)
b.append(2)
b.inOrder()
b.preOrder()
b.posOrder()