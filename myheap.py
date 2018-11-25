import heapq
import grade

class MyHeap(object):
    def __init__(self, initial = None, key = lambda x:-x):
        self.key = key
        if initial:
           self._data = [(key(item.scores["total"]), item) for item in initial]
           heapq.heapify(self._data)
        else:
           self._data = []

    def push(self, item):
        heapq.heappush(self._data, (self.key(item.scores["total"]), item))

    def pop(self):
            return heapq.heappop(self._data)[1]