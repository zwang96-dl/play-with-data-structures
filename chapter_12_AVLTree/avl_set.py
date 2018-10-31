from chapter_12_AVLTree.base import SetBase
from chapter_12_AVLTree.avl_tree import AVLTree


class AVLSet(SetBase):
    def __init__(self):
        self._avl = AVLTree()

    def get_size(self):
        return self._avl.get_size()

    def is_empty(self):
        return self._avl.is_empty()

    def add(self, key):
        return self._avl.add(key, None)

    def contains(self, key):
        return self._avl.contains(key)

    def remove(self, key):
        return self._avl.remove(key)

