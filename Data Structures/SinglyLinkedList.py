#Defining the Node class
class Node:

    def __init__(self,data,next=None):
        self.data=data
        self.next=next

    def __str__(self):
        return str(self.data)

#Defining the SinglyLinkedList class
class SLL:

    # Initializing the constructor
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0
        self.__trav=None

    # Returning the size of the linked list
    def size(self):
        return self.__size

    # Checking if the linked list is empty
    def isEmpty(self):
        return self.__size==0

    # Returning the string conversion of Linked list
    def __str__(self):
        l=[]
        te=self.__head
        while te is not None:
            l.append(te.data)
            te=te.next
        return '->'.join(map(str,l))

    # Function to get the head 
    # (Used in merge and interleave functions)
    def getHead(self):
        return self.__head

    # Function to set the head 
    # (Used in split function)
    def setHead(self,head):
        self.__head=head

    # Appending at the last
    def append(self,data):
        node = Node(data)
        if self.isEmpty():
            self.__head=node
            self.__tail=node
        else:
            self.__tail.next=node
            self.__tail=node
        self.__size+=1

    # Appending at the beginning
    def prepend(self,data):
        node=Node(data)
        if self.isEmpty():
            self.append(data)
        else:
            node.next=self.__head
            self.__head=node
        self.__size+=1

    # Appending at specified index
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

    # Removing from the first
    def removeFirst(self):
        if self.isEmpty():
            raise Exception("Empty Linked List")
        temp=self.__head
        self.__head=self.__head.next
        del(temp)
        self.__size-=1

    # Removing from the last
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

    # Removing from specified index
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

    # Rotating the list once towards right
    # Used in rotating k times function
    def rotateOnce(self):
        if self.isEmpty():
            raise Exception("Empty list!")
        else:
            temp=self.__head
            while temp.next.next:
                temp=temp.next
            self.__tail.next=self.__head
            self.__head=self.__tail
            temp.next=None
            self.__tail=temp

    # Rotating the list k times towards right
    def rotate(self,k):
        if self.isEmpty():
            raise Exception("Empty list!")
        else:
            for i in range(k):
                self.rotateOnce()

    # Finding the middle index
    def midInd(self):
        if self.isEmpty():
            raise Exception("Empty list!")
        else:
            fast=self.__head
            ind=0
            while fast and fast.next:
                ind+=1
                fast=fast.next.next
            return ind

    # Searching the required element
    def find(self,x):
        if self.isEmpty():
            raise Exception('Empty list!')
        else:
            temp=self.__head
            ind=0
            while temp:
                if temp.data==x:
                    return ind
                temp=temp.next
                ind+=1
            return -1

    # Splitting the Linked list into 2
    def split(self,ind):
        if self.isEmpty():
            raise Exception("Empty list!")
        else:
            temp=self.__head
            l1=temp
            i=0
            while i<ind:
                temp=temp.next
                i+=1
            l2=temp.next
            temp.next=None
            sll1=SLL()
            sll2=SLL()
            sll1.setHead(l1)
            sll2.setHead(l2)
            return (sll1,sll2)

    # Iter function
    def __iter__(self):
        self.__trav=self.__head
        return self

    # Next function
    def __next__(self):
        if self.__trav is None:
            raise StopIteration
        x=self.__trav.data
        self.__trav=self.__trav.next
        return x

    # Reversing the linked list
    def reverse(self):
        if self.isEmpty():
            raise Exception("Empty List!")
        else:
            prev=None
            cur=self.__head
            self.__tail=cur
            while cur:
                nxt=cur.next
                cur.next=prev
                prev=cur
                cur=nxt
            self.__head=prev

    # Interleaving 2 linked lists
    def interleave(self,ll):
        l2=ll.getHead()
        if l2 is None:
            pass
        else:
            l1=self.__head
            copy=l1
            l11=l1.next
            l22=l2.next
            while l1 and l2:
                l1.next=l2
                l2.next=l11
                l1=l11
                l2=l22
                l11=l11.next
                if l22:
                    l22=l22.next
            self.__head=copy

    # Merging 2 linked lists
    def merge(self,ll):
        l2=ll.getHead()
        if l2 is None:
            pass
        else:
            l1=self.__head
            if l1.data<l2.data:
                temp=l1
                l1=l1.next
            else:
                temp=l2
                l2=l2.next
            copy=temp
            while l1 and l2:
                if l1.data<l2.data:
                    temp.next=l1
                    l1=l1.next
                    temp=temp.next
                else:
                    temp.next=l2
                    l2=l2.next
                    temp=temp.next
            if l1 is not None:
                temp.next=l1
            else:
                temp.next=l2
            self.__head=copy



sll=SLL()
sll.append(1)
sll.append(5)
sll.append(9)
sll.append(2)
print(sll)
sll2=SLL()
sll2.append(6)
sll2.append(2)
print(sll2)
sll.interleave(sll2)
print(sll)
sll1,sll2=sll.split(1)
print(sll1," ",sll2)