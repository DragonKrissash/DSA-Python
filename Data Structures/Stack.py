class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class Stack:
    def __init__(self):
        self.sz=0
        self.head=None

    def size(self):
        return self.sz

    def isEmpty(self):
        return self.sz==0

    def push(self,data):
        node=Node(data,self.head)
        self.head=node
        self.sz+=1

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack underflow!")
        else:
            temp=self.head
            data=temp.data
            del(temp)
            self.head=self.head.next
            self.sz-=1
            return data

    def top(self):
        if self.isEmpty():
            raise Exception("Stack underflow")
        else:
            return self.head.data

    def __str__(self):
        l=[]
        trav=self.head
        while trav:
            l.append(str(trav.data))
            trav=trav.next
        return '->'.join(l)

    def insertAtBottom(self,x):
        if self.isEmpty():
            self.push(x)
        else:
            y=self.pop()
            self.insertAtBottom(x)
            self.push(y)

    def reverse(self):
        if self.isEmpty():
            pass
        else:
            y=self.pop()
            self.reverse()
            self.insertAtBottom(y)

    def sortedInsert(self,x):
        if self.isEmpty() or self.top()<=x:
            self.push(x)
        else:
            y=self.pop()
            self.sortedInsert(x)
            self.push(y)

    def sort(self):
        if self.isEmpty():
            pass
        else:
            y=self.pop()
            self.sort()
            self.sortedInsert(y)

st=Stack()
st.push(10)
st.push(6)
st.push(8)
print(st)
st.insertAtBottom(1)
print(st)
st.sortedInsert(5)
print(st)
st.sort()
print(st)