class Node:
    def __init__(self,val=0,key=0,next=None,prev=None):
        self.val=val
        self.next=next
        self.prev=prev
        self.key=key

class LRUCache:
    def __init__(self,cap):
        self.cap=cap
        self.head=None
        self.tail=None
        self.map={}
        self.sz=0

    def get(self,key):
        if self.sz==0 or key not in self.map:
            return None
        self.__use(self.map[key])
        return self.map[key].val

    def put(self,key,val):
        if self.sz<self.cap:
            if self.append(key,val):
                self.sz+=1
        else:
            temp=self.tail
            self.tail=self.tail.prev
            self.tail.next=None
            self.map.pop(temp.key)
            self.append(key,val)
            del temp

    def append(self,key,val):
        if self.head is None:
            node=Node(val,key)
            self.map[key]=node
            self.head=node
            self.tail=node
            return True

        if key not in self.map:
            node=Node(val,key)
            self.map[key]=node
            node.next=self.head
            self.head.prev=node
            self.head=node
            return True
        return False


    def __use(self,node):
        if node.next is not None and node.prev is not None:
            node.next.prev=node.prev
            node.prev.next=node.next
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
        elif node.next is None and node.prev is not None:
            self.tail=node.prev
            self.tail.next=None
            node.next=self.head
            self.head.prev=node
            self.head=node
        elif node.prev is None and node.next is not None:
            pass


    def __str__(self):
        l=[]
        temp=self.head
        while temp:
            l.append(str(temp.val))
            temp=temp.next
        return '->'.join(l)

l=LRUCache(3)
l.put(5,5)
l.put(1,1)
l.put(2,2)
l.put(3,3)
l.put(4,4)
l.get(2)
l.put(0,0)
l.get(4)
print(l)

