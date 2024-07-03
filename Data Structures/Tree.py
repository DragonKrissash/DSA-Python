class Node:
    def __init__(self,data=0,left=None,right=None,parent=None):
        self.data=data
        self.left=left
        self.right=right
        self.parent=parent

    def __str__(self):
        return str(self.data)

root=Node(1)
node1=Node(2,parent=root)
root.left=node1
node2=Node(3,parent=node1)
node1.left=node2
node4=Node(4,parent=root)
root.right=node4
node5=Node(5,parent=node4)
node4.right=node5
node6=Node(6,parent=node2)
node2.right=node6
node3=Node(3,parent=node1)
node1.right=node3
print(node3.right)