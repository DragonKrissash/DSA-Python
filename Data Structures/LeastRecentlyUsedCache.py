# class LRUCache:
#
#     def __init__(self, capacity: int):
#         from collections import deque
#         self.cap = capacity
#         self.qkeys = deque()
#         self.dict = {}
#         self.size = 0
#
#     def get(self, key: int) -> int:
#         if self.size == 0 or self.dict[key]=="#":
#             return -1
#         else:
#
#             return self.dict[key]
#
#     def put(self, key: int, value: int) -> None:
#         if self.cap == self.size:
#             back = self.qkeys.pop()
#             self.dict[back] = "#"
#             self.dict[key] = value
#             self.qkeys.appendleft(key)
#         else:
#             self.dict[key] = value
#             self.qkeys.appendleft(key)
#             self.size += 1
#
# # Your LRUCache object will be instantiated and called as such:
# # obj = LRUCache(capacity)
# # param_1 = obj.get(key)
# # obj.put(key,value)
from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.cap:
            self.cache.popitem(last=False)