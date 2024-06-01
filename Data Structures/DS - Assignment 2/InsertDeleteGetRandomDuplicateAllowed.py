# submissionId=1273812148

# import random
# class RandomizedCollection:
#
#     def __init__(self):
#         self.lst = []
#         self.ind = {}
#         self.fre={}
#
#     def find(self, val):
#         if val in self.ind:
#             return True
#         else:
#             return False
#
#     def insert(self, val: int) -> bool:
#         if not self.find(val):
#             self.ind[val] = len(self.lst)
#             self.fre[val] = 1
#             self.lst.append(val)
#             return True
#         self.fre[val]+=1
#         return False
#
#     def remove(self, val: int) -> bool:
#         if self.find(val):
#             if self.fre[val] > 1:
#                 self.fre[val]-=1
#             else:
#                 i=self.ind[val]
#                 self.lst[1]=self.lst[-1]
#                 self.ind[self.lst[-1]]=i
#                 self.fre[self.lst[-1]]+=1
#                 self.lst.pop()
#                 del(self.ind[val])
#                 del(self.fre[val])
#             return True
#         else:
#             return False
#
#     def getRandom(self) -> int:
#         return random.choices(self.lst,weights=list(self.fre.values()),k=1)[0]

import random
class RandomizedCollection:

    def __init__(self):
        from sortedcontainers import SortedList
        from collections import defaultdict
        self.lst=SortedList([])
        self.ind=defaultdict(lambda:0)

    def insert(self, val: int) -> bool:
        self.lst.append(val)
        self.ind[val]+=1
        return self.ind[val]==1

    def remove(self, val: int) -> bool:
        if self.ind[val]>0:
            self.lst.discard(val)
            self.ind[val]-=1
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.lst)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()