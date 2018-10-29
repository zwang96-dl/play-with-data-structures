from chapter_04_LinkedList.linkedlist import LinkedList
from chapter_07_Set_Map.base import SetBase


class LinkedListSet(SetBase):
    def __init__(self):
        self._list = LinkedList()

    def get_size(self):
        return self._list.get_size()

    def is_empty(self):
        return self._list.is_empty()

    def contains(self, e):
        return self._list.contains(e)

    def add(self, e):
        if self.contains(e):
            return
        self._list.add_first(e)

    def remove(self, e):
        self._list.remove(e)


if __name__ == '__main__':
    words = ''
    with open('./chapter_07_Set_Map/shakespeare.txt', 'r') as f:
        words = f.read()
    words = words.split()

    from time import time
    start_time = time()
    bst_set = LinkedListSet()
    for word in words:
        bst_set.add(word)
    
    print('Total words: ', len(words))
    print('Unique words: ', bst_set.get_size())
    print('Contains word "they": ', bst_set.contains('they'))
    ## 耗时100秒左右
    print('Total time: {} seconds'.format(time() - start_time))


