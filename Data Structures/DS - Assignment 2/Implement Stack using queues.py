# submissionId=1273380615

class MyStack:

    def __init__(self):
        from queue import Queue
        self.q1=Queue()
        self.q2=Queue()
        self.sze=0

    def push(self, x: int) -> None:
        if self.q1.empty():
            self.q1.put(x)
        else:
            while not self.q1.empty():
                self.q2.put(self.q1.get())
            self.q1.put(x)
            while not self.q2.empty():
                self.q1.put(self.q2.get())
        self.sze+=1
    def pop(self) -> int:
        if self.empty():
            raise Exception('Empty stack')
        else:
            x=self.q1.get()
        self.sze-=1
        return x


    def top(self) -> int:
        if self.empty():
            raise Exception('Empty stack')
        else:
            x = self.q1.queue[0]
        return x

    def empty(self) -> bool:
        return self.sze==0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()