class Entry:
    def __init__(self,key,val):
        self.key=key
        self.val=val

class HashMap:
    def __init__(self):
        self.cap=10
        self.size=0
        self.data=[[] for i in range(self.cap)]
        self.threshold=0.5

    def isEmpty(self):
        return self.size==0

    def resize(self):
        self.cap=self.cap*2
        newData=[[]for i in range(self.cap)]
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                hashInd=hash(self.data[i][j].key)%self.cap
                newData[hashInd].append(self.data[i][j])
        temp=self.data
        self.data=newData
        del temp

    def insert(self,key,val):
        hashInd=hash(key)%self.cap
        e=Entry(key,val)
        if self.size/self.cap == self.threshold:
            self.resize()
            self.insert(key,val)
        else:
            if self.size==0:
                self.data[hashInd].append(e)
            else:
                for i in range(len(self.data[hashInd])):
                    if self.data[hashInd][i].key == key:
                        self.data[hashInd][i].val=val
                        return
                self.data[hashInd].append(e)
            self.size+=1

    def get(self,key):
        hashInd=hash(key)%self.cap
        for i in range(len(self.data[hashInd])):
            if self.data[hashInd][i].key==key:
                return self.data[hashInd][i].val
        return 0

    def __str__(self):
        if self.isEmpty():
            return ""
        else:
            data={}
            for i in range(len(self.data)):
                for j in range(len(self.data[i])):
                    data[self.data[i][j].key]=self.data[i][j].val
            return (str(data))

    def remove(self,key):
        if self.size==0:
            return -1
        hashInd=hash(key)%self.cap
        for i in range(len(self.data[hashInd])):
            if self.data[hashInd][i].key==key:
                x=self.data[hashInd][i].val
                e=self.data[hashInd][i]
                self.data[hashInd][i]=self.data[hashInd][-1]
                self.data[hashInd][-1]=e
                self.data[hashInd].pop()
                del e
                self.size-=1
                return x
        return -1
mp=HashMap()
mp.insert('a',1)
mp.insert('b',2)
mp.insert('a',3)
mp.insert('c',4)
print(mp.cap)
mp.insert('d',5)
print(mp)
mp.insert('e',6)
mp.insert('e',6)
mp.insert('e',6)
print(mp.cap)
print(mp)
print(mp.remove('a'))
print(mp.remove('g'))