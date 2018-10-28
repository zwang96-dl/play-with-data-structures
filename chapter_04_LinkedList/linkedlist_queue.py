from chapter_03_Stack_Queue.base import QueueBase
from chapter_03_LinkedList.linkedlist import LinkedList


class LinkedListQueue(QueueBase):
    """头出尾入"""
    class _Node:
        def __init__(self, e=None, node_next=None):
            self.e = e
            self.next = node_next

        def __str__(self):
            return str(self.e)

        def __repr__(self):
            return self.__str__()

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def enqueue(self, e):
        # 其实也说明了self._head也为空
        if not self._tail:
            self._tail = self._Node(e)
            self._head = self._tail
        else:
            self._tail.next = self._Node(e)
            self._tail = self._tail.next
        self._size += 1

    def dequeue(self):
        if (self.is_empty()):
            raise ValueError('Can not dequeue from an empty queue.')
        ret = self._head
        self._head = self._head.next
        ret.next = None
        # 特殊情况，如果链表中只有一个元素，此时head和tail应该都为空
        if not self._head:
            self._tail = None
        self._size -= 1
        return ret.e

    def get_front(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        return self._head.e

    def __str__(self):
        curr = self._head
        data = []
        while curr:
            data.append(str(curr.e))
            curr = curr.next
        return '<chapter_03_LinkedList.linkedlist_queue.LinkedListQueue>: (Tail) ' + \
            ' <-> '.join(data) + ' (Head)'
        

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    queue = LinkedListQueue()
    queue.enqueue(1)
    queue.enqueue(4)
    queue.enqueue(100)
    queue.enqueue(9)
    print(queue)

    queue.dequeue()
    print(queue)

    queue.enqueue('zhe')
    print(queue)

    queue.dequeue()
    print(queue)