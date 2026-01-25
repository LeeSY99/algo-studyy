class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []
        

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if self.max_heap and self.min_heap:
            if -self.max_heap[0] > self.min_heap[0]:
                temp_min = heapq.heappop(self.min_heap)
                temp_max = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, temp_max)
                heapq.heappush(self.max_heap, -temp_min)
        

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()