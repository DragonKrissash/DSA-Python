class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

    def __str__(self):
        return str(self.data)

class StackLinkedList:

    def __init__(self):
        self.__size=0
        self.__head=None

    def size(self):
        return self.__size

    def isEmpty(self):
        if self.__size==0:
            return True
        else:
            return False

    def push(self,data):
        node=Node(data)
        if self.isEmpty():
            self.__head=node
        else:
            node.next=self.__head
            self.__head=node
        self.__size+=1

    def pop(self):
        if self.isEmpty():
            raise Exception("Empty stack")
        else:
            temp=self.__head
            self.__head=self.__head.next
            del(temp)
        self.__size-=1

    def __str__(self):
        if self.isEmpty():
            return ""
        else:
            l=[]
            temp=self.__head
            while temp:
                l.append(temp.data)
                temp=temp.next
            return '->'.join(map(str,l))

sll=StackLinkedList()
sll.push(5)
sll.push(10)
sll.push('Krishna')
print(sll)
sll.pop()
print(sll)
