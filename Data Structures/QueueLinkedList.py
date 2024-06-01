class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
    def __str__(self):
        return self.data

class QueueLinkedList:

    def __init__(self):
        self.__head=None
        self.__size=0
        self.__tail=None

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
            self.__tail=node
        else:
            self.__tail.next=node
            self.__tail=node
        self.__size+=1

    def pop(self):
        if self.isEmpty():
            raise Exception("Empty Linked List")
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
            return " | ".join(map(str,l))

qll=QueueLinkedList()
qll.push(10)
qll.push(20)
qll.push(30)
print(qll)
qll.pop()
print(qll)


