class Entry:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.hash=hash(key)

    def __str__(self):
        return str(self.key)+" : "+str(self.value)

class HT:
    def __init__(self):
        self.size=0
        self.cap=12
        self.data=[None for i in range(self.cap)]

    def prob(self,x):
        return 5*x

    def getSize(self):
        return self.size

    def insert(self,key,value):
        entry=Entry(key,value)
        index=entry.hash % self.cap
        i=0
        while True:
            ind=(index+self.prob(i)) % self.cap
            if self.data[ind]==None:
                self.data[ind]=entry
                break
            i+=1

    def find(self,key):
        index=hash(key)%self.cap
        for i in range(self.cap):
            ind=(index+self.prob(i))%self.cap
            if self.data[ind] is not None:
                return True
        return False

    def remove(self,key):
        if self.find(key):
            index=hash(key)%self.cap
            for i in range(self.cap):
                ind=(index+self.prob(i))%self.cap
                if self.data[ind] is not None and self.data[ind].key==key:
                    self.data[ind]=None
                    return True
        else:
            return False

    def __str__(self):
        for i in range(self.cap):
            print(self.data[i])
        return ""

ht=HT()
ht.insert('roll 1',123)
ht.insert('roll 2',432)
ht.insert('2',1)
print(ht.remove('2'))
print(ht)