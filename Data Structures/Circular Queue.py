class Node(object):
    def __init__(self,data=0,next=None):
        self.data=data
        self.next=next

class MyCircularQueue(object):

    def __init__(self, k: int):
        self.head=None
        self.tail=None
        self.size=0
        self.cap=k

    def enQueue(self, value: int) -> bool:
        if self.size==self.cap:
            return False
        elif self.size==0:
            node=Node(data=value)
            self.head=node
            self.tail=node
            self.head.next=self.head
            self.size+=1
            return True
        else:
            node=Node(data=value,next=self.head)
            self.tail.next=node
            self.tail=node
            self.size+=1
            return True

    def deQueue(self) -> bool:
        if self.size==0:
            return False
        else:
            temp=self.head
            self.head=self.head.next
            self.tail.next=self.head
            del temp
            self.size-=1
            return True

    def Front(self) -> int:
        if self.size==0:
            return -1
        else:
            return self.head.data

    def Rear(self) -> int:
        if self.size==0:
            return -1
        else:
            return self.tail.data

    def isEmpty(self) -> bool:
        return self.size==0

    def isFull(self) -> bool:
        return self.size==self.cap

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()