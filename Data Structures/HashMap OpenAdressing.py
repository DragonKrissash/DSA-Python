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
        print(f'Inserting key {str(key)}')
        while True:
            ind=(index+self.prob(i)) % self.cap
            print(f'Trying index: {str(ind)}')
            if self.data[ind]==None:
                self.data[ind]=entry
                print(f'Inserting at index : {ind}')
                break
            i+=1

    def print(self):
        for i in range(self.cap):
            print(self.data[i],sep=',')

ht=HT()
ht.insert('roll 1',123)
ht.insert('roll 2',432)
ht.print()