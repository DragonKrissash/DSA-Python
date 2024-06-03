class Node:
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next

class CircularQueue:

    def __init__(self):
        self.__sze=0
        self.__head=None
        self.__tail=None

    def size(self):
        return self.__sze

    def isEmpty(self):
        return self.__sze==0

    def enque(self,data):
        node = Node(data,next=self.__head)
        if self.isEmpty():
            self.__tail=node
            self.__head=node
            self.__head.next=self.__tail
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
            self.__tail.next=self.__head
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
            x=temp.data
            temp=self.__head.next
            while temp is not self.__head:
                l.append(x)
                x = temp.data
                temp=temp.next
            l.append(x)
            return '->'.join(map(str,l))

q=CircularQueue()
q.enque(10)
q.enque(12)
q.enque(13)
q.enque(16)
q.enque(20)
print(q)

