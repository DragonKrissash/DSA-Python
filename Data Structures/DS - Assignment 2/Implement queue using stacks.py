# submissionId=1273388022

class MyQueue:

    def __init__(self):
        self.st1=[]
        self.st2=[]
        self.sze=0

    def push(self, x: int) -> None:
        self.st1.append(x)
        self.sze+=1

    def pop(self) -> int:
        if self.empty():
            raise Exception('Empty queue')
        else:
            while not len(self.st1)==0:
                self.st2.append(self.st1.pop())
            x=self.st2.pop()
            while not len(self.st2) == 0:
                self.st1.append(self.st2.pop())
        self.sze-=1
        return x

    def peek(self) -> int:
        if self.empty():
            raise Exception('Empty queue')
        else:
            while not len(self.st1)==0:
                self.st2.append(self.st1.pop())
            x=self.st2[-1]
            while not len(self.st2) == 0:
                self.st1.append(self.st2.pop())
        return x
    def empty(self) -> bool:
        return self.sze==0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()