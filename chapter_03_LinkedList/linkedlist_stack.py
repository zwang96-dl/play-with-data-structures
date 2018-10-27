from chapter_02_Array.base import StackBase
from chapter_03_LinkedList.linkedlist import LinkedList

class LinkedListStack(StackBase):
    def __init__(self):
        self._list = LinkedList()

    def get_size(self):
        return self._list.get_size()

    def is_empty(self):
        return self._list.is_empty()

    def push(self, e):
        self._list.add_first(e)

    def pop(self):
        return self._list.remove_first()

    def peek(self):
        return self._list.get_first()

    def __str__(self):
        curr = self._list._dummy_head.next
        data = []
        while curr:
            data.append(str(curr.e))
            curr = curr.next
        return '<chapter_03_LinkedList.linkedlist_stack.LinkedListStack>: (Top) ' + ' -> '.join(data)

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    linkedlist_stack = LinkedListStack()
    linkedlist_stack.push(1)
    linkedlist_stack.push(3)
    linkedlist_stack.push(999)
    print(linkedlist_stack)
    print(linkedlist_stack.pop())
    print(linkedlist_stack)