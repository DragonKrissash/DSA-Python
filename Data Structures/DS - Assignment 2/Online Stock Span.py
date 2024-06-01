# submissionId=1274199725

class StockSpanner(object):

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        ele = 1
        while not len(self.prices) == 0 and self.prices[-1][0] <= price:
            ele += self.prices[-1][1]
            self.prices.pop()
        self.prices.append((price, ele))
        return ele

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)