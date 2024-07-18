class Node:
    def __init__(self,value=0) -> None:
        self.value=value
        self.ht=0
        self.bf=0
        self.left=None
        self.right=None

class AVLTree:
    def __init__(self) -> None:
        self.__root=None
        self.__noOfNodes=0

    def find(self,value):
        return self.__find(self.__root,value)

    def __find(self,node,value):
        if node is None:
            return False

        if node.value==value:
            return True

        if value>node.value:
            return self.__find(node.right,value)
        else:
            return self.__find(node.left,value)

    def insert(self,value):
        if value==None:
            return False

        if self.find(value):
            return False
        else:
            self.__root=self.__insert(self.__root,value)
            self.__noOfNodes+=1
            return True

    def __insert(self,node,value):
        if node is None:
            return Node(value)

        if node.value<value:
            node.right=self.__insert(node.right,value)
        else:
            node.left=self.__insert(node.left,value)

        self.__update(node)
        return self.__balance(node)

    def __update(self,node):
        leftHeight=-1
        rightHeight=-1

        if node.left is not None:
            leftHeight=node.left.ht
        if node.right is not None:
            rightHeight=node.right.ht

        node.ht=1+max(leftHeight,rightHeight)
        node.bf=rightHeight-leftHeight

    def __balance(self,node):
        if node.bf==2:
            if node.right.bf>0:
                return self.__rightRightCase(node)
            else:
                return self.__rightLeftCase(node)

        elif node.bf==-2:
            if node.left.bf<0:
                return self.__leftLeftCase(node)
            else:
                return self.__leftRightCase(node)

        else:
            return node

    def __rightRightCase(self,node):
        return self.__leftRotate(node)

    def __leftLeftCase(self,node):
        return self.__rightRotate(node)
    def __rightLeftCase(self,node):
        node.right=self.__rotateRight(node)
        return self.__rightRightCase(node)

    def __leftRightCase(self,node):
        node.left=self.__rotateLeft(node.left)
        return self.__leftLeftCase(node)

    def __rotateRight(self,node):
        B=node.left
        node.left=B.right
        B.right=node
        self.__update(node)
        self.__update(B)
        return B

    def __rotateLeft(self,node):
        B=node.right
        node.right=B.left
        B.left=node
        self.__update(node)
        self.__update(B)
        return B

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