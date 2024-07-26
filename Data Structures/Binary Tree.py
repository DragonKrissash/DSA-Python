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

    def remove(self,value):
        if value is None:
            return False
        if not self.find(value):
            return False
        else:
            self.__root=self.__remove(self.__root,value)
            self.__noOfNodes-=1
            return True

    def __remove(self,node,value):
        if node.value==value:
            if node.right is None and node.left is None:
                del(node)
                return None
            elif node.left is None:
                temp=node.right
                del node
                return temp
            elif node.right is None:
                temp=node.left
                del node
                return temp
            else:
                suc=node.left
                while suc.right is not None:
                    suc=suc.right
                node.value=suc.value
                node.left=self.__remove(node.left,suc.value)
                return node
        elif node.value>value:
            node.left=self.__remove(node.left,value)
        else:
            node.right=self.__remove(node.right,value)

        self.__update(node)
        return self.__balance(node)

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