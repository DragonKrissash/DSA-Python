# submissionId=1274240390

class BrowserHistory:

    def __init__(self, homepage: str):
        self.webpages = []
        self.webpages.append(homepage)
        self.currindex = 0

    def visit(self, url: str) -> None:
        if self.currindex == len(self.webpages) - 1:
            self.webpages.append(url)
            self.currindex += 1
        else:
            self.currindex += 1
            self.webpages[self.currindex] = url
        while len(self.webpages) > self.currindex + 1:
            self.webpages.pop()

    def back(self, steps: int) -> str:
        if self.currindex - steps < 0:
            self.currindex = 0
            return self.webpages[0]
        else:
            self.currindex = self.currindex - steps
            return self.webpages[self.currindex]

    def forward(self, steps: int) -> str:
        if self.currindex + steps > len(self.webpages) - 1:
            self.currindex = len(self.webpages) - 1
            return self.webpages[self.currindex]
        else:
            self.currindex += steps
            return self.webpages[self.currindex]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)