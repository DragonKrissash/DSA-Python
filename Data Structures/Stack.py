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

st=Stack()
st.push(7)
st.push(9)
print(st.size())
st.push(189)
print(st)
print(st.top())
print(st.pop())
print(st)