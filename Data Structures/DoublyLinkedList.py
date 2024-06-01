class Node:
    def __init__(self,data,prev=None,next=None):
        self.data=data
        self.prev=prev
        self.next=next

    def __str__(self):
        return str(self.data)

class DLL:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0

    def size(self):
        return self.__size

    def __str__(self):
        l=[]
        trap=self.__head
        while trap is not None:
            l.append(trap.data)
            trap=trap.next
        return '<=>'.join(map(str,l))

    def isEmpty(self):
        return self.size()==0

    def append(self,data):
        newNode=Node(data)
        if self.isEmpty():
            self.__head=newNode
            self.__tail=newNode
        else:
            newNode.prev=self.__tail
            self.__tail.next=newNode
            self.__tail=newNode
        self.__size+=1

    def addFirst(self,data):
        node=Node(data)
        if self.isEmpty():
            self.__head=node
            self.__tail=node
        else:
            node.next=self.__head
            self.__head.prev=node
            self.__head=node
        self.__size+=1

    def addAt(self,ind,data):
        if ind<0 or ind>self.__size:
            raise Exception('Invalid Index')
        if ind==0:
            self.addFirst(data)
        elif ind==self.__size:
            self.append(data)
        else:
            id=0
            temp=self.__head
            while id !=ind-1:
                id+=1
                temp=temp.next
            node=Node(data,temp,temp.next)
            temp.next=node
            node.next.prev=node
        self.__size+=1

    def removeFirst(self):
        if self.isEmpty():
            raise Exception('Empty linked list')
        temp=self.__head
        self.__head=self.__head.next
        self.__head.prev=None
        del(temp)
        self.__size-=1

    def removeEnd(self):
        if self.isEmpty():
            raise Exception('Empty Linked list')
        temp=self.__tail
        self.__tail=self.__tail.prev
        self.__tail.next=None
        del(temp)
        self.__size-=1

    def removeAt(self,ind):
        if self.isEmpty():
            raise Exception('Empty Linked list')
        if ind<0 or ind>self.__size:
            raise Exception('Index out of bound!')
        else:
            id=0;
            temp=self.__head
            while id!=ind-1:
                id+=1
                temp=temp.next
            t1=temp.next
            temp.next=temp.next.next
            temp.next.prev=temp
            del(t1)
        self.__size-=1
dll=DLL()
dll.append(13)
dll.append("krishna")
dll.addFirst('Kishore')
dll.addAt(1,25)
print(dll)
dll.removeAt(1)
print(dll)
