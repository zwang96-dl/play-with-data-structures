from chapter_12_AVLTree.base import MapBase
from chapter_12_AVLTree.avl_tree import AVLTree


class AVLMap(MapBase):
    def __init__(self):
        self._avl = AVLTree()

    def get_size(self):
        return self._avl.get_size()

    def is_empty(self):
        return self._avl.is_empty()

    def add(self, key, value):
        return self._avl.add(key, value)

    def contains(self, key):
        return self._avl.contains(key)

    def getter(self, key):
        return self._avl.getter(key)

    def setter(self, key, value):
        return self._avl.setter(key, value)

    def remove(self, key):
        return self._avl.remove(key)

