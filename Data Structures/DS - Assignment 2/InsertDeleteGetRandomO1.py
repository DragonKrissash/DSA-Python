# submissionId=1273781062
import random
class RandomizedSet:

    def __init__(self):
        self.lst=[]
        self.ind={}

    def find(self,val):
        if val in self.ind:
            return True
        else:
            return False

    def insert(self, val: int) -> bool:
        if self.find(val):
            return False
        self.ind[val]=len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
            if not self.find(val):
                return False
            i=self.ind[val]
            self.lst[i]=self.lst[-1]
            self.ind[self.lst[-1]]=i
            self.lst.pop()
            del(self.ind[val])
            return True


    def getRandom(self) -> int:
        return random.choice(self.lst)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()