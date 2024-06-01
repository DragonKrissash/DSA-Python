class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    def __str__(self):
        return str(self.data)

class DeQueueLinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0

    def size(self):
        return self.__size

    def isEmpty(self):
        if self.__size==0:
            return True
        else:
            return False

    def pushBack(self,data):
        node=Node(data)
        if self.isEmpty():
            self.__head=node
            self.__tail=node
        else:
            self.__tail.next=node
            node.next=self.__head
            self.__tail=node
        self.__size+=1

    def pushFront(self,data):
        node=Node(data)
        if self.isEmpty():
            self.__head=node
            self.__tail=node
        else:
            self.__tail.next=node
            node.next=self.__head
            self.__head=node
        self.__size+=1

    def popBack(self):
        if self.isEmpty():
            raise Exception('Empty Dequeue')
        else:
            temp=self.__head
            while temp.next is not self.__tail:
                temp=temp.next
            self.__tail=temp
            temp=temp.next
            del(temp)
        self.__size-=1

    def popFront(self):
        if self.isEmpty():
            raise Exception('Empty Dequeue')
        else:
            temp=self.__head
            self.__head=self.__head.next
            self.__tail.next=self.__head
            del(temp)
        self.__size-=1

    def __str__(self):
        if self.isEmpty():
            return ""
        else:
            temp=self.__head.next
            l=[]
            l.append(self.__head.data)
            while temp is not self.__head:
                l.append(temp.data)
                temp=temp.next
            return '=>'.join(map(str,l))

dqll=DeQueueLinkedList()
dqll.pushBack(10)
dqll.pushBack(20)
dqll.pushBack(30)
print(dqll)
dqll.pushFront(40)
dqll.pushFront(50)
dqll.pushFront(60)
print(dqll)
dqll.popBack()
dqll.popFront()
print(dqll)