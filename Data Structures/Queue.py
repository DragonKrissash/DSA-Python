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
            del(temp)
        self.__sze-=1

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

q=Queue()
q.enque(10)
q.enque(12)
q.enque(13)
print(q)
q.deque()
print(q)
q.enque(16)
q.enque(20)
print(q.front())
print(q.back())
print(q.size())
print(q)

