class Node:

    def __init__(self,data,next=None):
        self.data=data
        self.next=next

    def __str__(self):
        return str(self.data)

class SLL:

    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0
        self.__trav=None

    def size(self):
        return self.__size

    def isEmpty(self):
        return self.__size==0

    def __str__(self):
        l=[]
        te=self.__head
        while te is not None:
            l.append(te.data)
            te=te.next
        return '->'.join(map(str,l))

    def append(self,data):
        node = Node(data)
        if self.isEmpty():
            self.__head=node
            self.__tail=node
        else:
            self.__tail.next=node
            self.__tail=node
        self.__size+=1

    def addFirst(self,data):
        node=Node(data)
        if self.isEmpty():
            self.append(data)
        else:
            node.next=self.__head
            self.__head=node
        self.__size+=1

    def addAt(self,ind,data):
        if self.isEmpty():
            raise Exception('Empty Linked List')
        if ind<0 or ind >self.__size:
            raise Exception('Index out of bound!')
        elif ind==0:
            self.addFirst(data)
        elif ind==self.__size:
            self.append(data)
        else:
            temp=self.__head
            id=0
            while id+1 != ind:
                id+=1
                temp=temp.next
            node=Node(data,temp.next)
            temp.next=node
        self.__size+=1

    def removeFirst(self):
        if self.isEmpty():
            raise Exception("Empty Linked List")
        temp=self.__head
        self.__head=self.__head.next
        del(temp)
        self.__size-=1

    def removeLast(self):
        if self.isEmpty():
            raise Exception('Empty Linked List')
        temp=self.__head
        while temp.next is not self.__tail:
            temp=temp.next
        self.__tail=temp
        self.__tail.next=None
        temp=temp.next
        del(temp)
        self.__size-=1

    def removeAt(self,ind):
        if self.isEmpty():
            raise Exception('Empty Linked List')
        if ind==0:
            self.removeFirst()
        elif ind==self.__size-1:
            self.removeLast()
        else:
            temp=self.__head
            id=0
            while id<ind-1:
                temp=temp.next
                id+=1
            te=temp.next
            temp.next= temp.next.next
            del(te)
            self.__size-=1

    def __iter__(self):
        self.__trav=self.__head
        return self

    def __next__(self):
        if self.__trav is None:
            raise StopIteration
        x=self.__trav.data
        self.__trav=self.__trav.next
        return x

sll=SLL()
sll.append(4)
sll.append(5)
sll.append(10)
sll.append(15)
print(sll)
for i in sll:
    print(i)