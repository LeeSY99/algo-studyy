n,m = map(int, input().split())

arr= list(map(int, input().split()))

import heapq

class PriorityQueue:
    def __init__(self):
        self.items = []

    def push(self, item):
        heapq.heappush(self.items, -item)

    def pop(self):
        return -heapq.heappop(self.items)

my_q = PriorityQueue()

for num in arr:
    my_q.push(num)

for _ in range(m):
    max_num = my_q.pop()
    # print(max_num)
    my_q.push(max_num - 1)

print(my_q.pop())