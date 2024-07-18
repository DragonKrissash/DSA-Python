class Node:
    def __init__(self,data=0,lNode=None,rNode=None):
        self.data=data
        self.lNode=lNode
        self.rNode=rNode

class BinarySearchTree:

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

    def insert(self,data):
        self.root=self.insert2(self.root,data)

    def insert2(self,root,data):
        if root is None:
            self.no_of_nodes+=1
            return Node(data)
        if data==root.data:
            return root
        if root.data<data:
            root.rNode=self.insert2(root.rNode,data)
            return root
        else:
            root.lNode=self.insert2(root.lNode,data)
            return root

b=BinarySearchTree()
b.insert(5)
b.insert(25)
b.insert(1)
b.insert(12)
b.insert(3)
b.insert(2)
b.inOrder()
b.preOrder()
b.posOrder()