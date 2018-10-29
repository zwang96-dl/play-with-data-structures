from chapter_03_Stack_Queue.base import QueueBase
from chapter_08_MaxHeap.max_heap import MaxHeap


class PriorityQueue(QueueBase):
    def __init__(self):
        self._max_heap = MaxHeap()

    def get_size(self):
        return self._max_heap.size()

    def is_empty(self):
        return self._max_heap.is_empty()

    def get_front():
        return self._max_heap.find_max()

    def enqueue(self, e):
        self._max_heap.add(e)

    def dequeue(self):
        return self._max_heap.extract_max()