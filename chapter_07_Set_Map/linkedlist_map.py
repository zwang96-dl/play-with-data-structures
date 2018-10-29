from chapter_07_Set_Map.base import MapBase


class LinkedListMap(MapBase):
    class _Node:
        def __init__(self, key=None, value=None, node_next=None):
            self.key = key
            self.value = value
            self.next = node_next

        def __str__(self):
            return "Key: {}, Value: {}".format(str(self.key), str(self.value))

        def __repr__(self):
            return self.__str__()

    def __init__(self):
        self._dummy_head = self._Node()
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self.get_size() == 0

    def get_node(self, key):
        curr = self._dummy_head.next
        while curr:
            if curr.key == key:
                return curr
            curr = curr.next

    def contains(self, key):
        return self.get_node(key) is not None

    def getter(self, key):
        node = self.get_node(key)
        return node.value if node is not None else None

    def add(self, key, value):
        node = self.get_node(key)
        if not node:
            self._dummy_head.next = self._Node(key, value, self._dummy_head.next)
            self._size += 1
        else:
            node.value = value

    def setter(self, key, value):
        node = self.get_node(key)
        if not node:
            raise ValueError('Key "{}" doesn\'t exist!'.format(str(key)))
        node.value = value

    def remove(self, key):
        prev = self._dummy_head
        while prev.next:
            if prev.next.key == key:
                break
            prev = prev.next
        # 判断prev是否是break出来的
        if prev.next:
            del_node = prev.next
            prev.next = del_node.next
            del_node.next = None
            return del_node.value


if __name__ == '__main__':
    words = ''
    with open('./chapter_07_Set_Map/shakespeare.txt', 'r') as f:
        words = f.read()
    words = words.split()

    from time import time
    start_time = time()
    linkedlist_map = LinkedListMap()
    for word in words:
        if linkedlist_map.contains(word):
            linkedlist_map.setter(word, linkedlist_map.getter(word) + 1)
        else:
            linkedlist_map.add(word, 1)
    
    print('Total words: ', len(words))
    print('Unique words: ', linkedlist_map.get_size())
    print('Contains word "they": ', linkedlist_map.contains('they'))
    ## 耗时290秒左右
    print('Total time: {} seconds'.format(time() - start_time))
