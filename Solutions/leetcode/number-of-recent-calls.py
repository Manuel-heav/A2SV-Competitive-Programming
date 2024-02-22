class RecentCounter:

    def __init__(self):
        self.queue = []
        self.headIndex = 0

    def ping(self, t: int) -> int:
        self.queue.append(t)
        range1 = t-3000
        range2 = t
        while self.queue[0] < range1:
            self.queue = self.queue[1:]
        
        return len(self.queue)
      


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)