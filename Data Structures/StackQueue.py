class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next

class Queue:

    def __init__(self):
        self.__sze=0
        self.__head=None
        self.__tail=None

    def size(self):
        return self.__sze

    def isEmpty(self):
        return self.__sze==0

    def enque(self,data):
        node = Node(data)
        if self.isEmpty():
            self.__tail=node
            self.__head=node
        else:
            self.__tail.next=node
            self.__tail=node
        self.__sze+=1

    def deque(self):
        if self.isEmpty():
            raise Exception("Empty queue")
        else:
            temp=self.__head
            self.__head=self.__head.next
            ret=temp.data
            del(temp)
        self.__sze-=1
        return ret

    def front(self):
        if self.isEmpty():
            raise Exception('Empty queue')
        else:
            return self.__head.data

    def back(self):
        if self.isEmpty():
            raise Exception('Empty queue')
        else:
            return self.__tail.data

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

class Stack:

    def __init__(self) -> None:
        self.q1=Queue()
        self.q2=Queue()
        self.sze=0

    def isEmpty(self):
        return self.sze==0
        

    def push(self,x):
        self.q1.enque(x)
        self.sze+=1

    def pop(self):
        if self.isEmpty():
            raise Exception('Empty stack!')
        else:
            while not self.q1.isEmpty():
                self.q2.enque(self.q1.deque())
            ret=self.q2.deque()
            while not self.q2.isEmpty():
                self.q1.enque(self.q2.deque())
        self.sze-=1
        return ret

s=Stack()
s.push(10)
s.push(15)
print(s.pop())