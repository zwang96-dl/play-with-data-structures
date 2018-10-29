from chapter_06_BST.bst import BST
from chapter_07_Set_Map.base import MapBase


class BSTMap(MapBase):
    class _Node:
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.left = None
            self.right = None

        def __str__(self):
            return "Key: {}, Value: {}".format(str(self.key), str(self.value))

        def __repr__(self):
            return self.__str__()

    def __init__(self):
        self._root = None
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add(self, key, value):
        self._root = self._add(self._root, key, value)

    def _add(self, node, key, value):
        if not node:
            self._size += 1
            return self._Node(key, value)
        if node.key == key:
            node.value = value
        elif node.key > key:
            node.left = self._add(node.left, key, value)
        else:
            node.right = self._add(node.right, key, value)
        return node

    def _get_node(self, node, key):
        if not node:
            return
        if node.key == key:
            return node
        elif node.key > key:
            return self._get_node(node.left, key)
        else:
            return self._get_node(node.right, key)

    def contains(self, key):
        return self._get_node(self._root, key) is not None

    def getter(self, key):
        node = self._get_node(self._root, key)
        return node.value if node is not None else None

    def setter(self, key, value):
        node = self._get_node(self._root, key)
        if not node:
            raise ValueError('Key "{}" doesn\'t exist!'.format(str(key)))
        node.value = value

    def remove(self, key):
        node = self._get_node(self._root, key)
        if not node:
            self._root = self._remove(self._root, key)
            return node.value

    # 删除以node为根的BST中键值为key的节点，递归算法
    # 返回删除节点后的新的BSTMap的根
    def _remove(self, node, key):
        # 递归终止
        if not node:
            return
        # 递归条件
        if node.key > key:
            node.left = self._remove(node.left, key)
            return node
        elif node.key < key:
            node.right = self._remove(node.right, key)
        else: # node.key == key
            if not node.left:
                right_node = node.right
                node.right = None
                self._size -= 1
                return right_node
            if not node.right:
                left_node = node.left
                node.left = None
                self._size -= 1
                return left_node
            # 如果左右子树均不为空
            # 找到比待删除节点大的最小节点，即待删除节点右子树的最小节点
            # 用这个节点顶替待删除节点的位置
            successor = self.minimum(node.right)
            successor.right = self._remove_min(node.right)
            successor.left = node.left
            node.left = node.right = None
            return successor

    def minimum(self):
        if self.is_empty():
            raise ValueError('BSTMap is empty!')
        self._minimum(self._root)

    def _minimum(self, node):
        if not node.left:
            return node
        return self._minimum(node.left)

    # 删除掉以node为根的BSTMap中的最小节点
    # 返回删除节点后新的BSTMap的根
    def _remove_min(self, node):
        # 递归终止
        if not node.left:
            right_node = node.right
            node.right = None
            self._size -= 1
            return right_node
        node.left = self._remove_min(node.left)
        return node


if __name__ == '__main__':
    words = ''
    with open('./chapter_07_Set_Map/shakespeare.txt', 'r') as f:
        words = f.read()
    words = words.split()

    from time import time
    start_time = time()
    bst_map = BSTMap()
    for word in words:
        if bst_map.contains(word):
            bst_map.setter(word, bst_map.getter(word) + 1)
        else:
            bst_map.add(word, 1)
    
    print('Total words: ', len(words))
    print('Unique words: ', bst_map.get_size())
    print('Contains word "they": ', bst_map.contains('they'))
    ## 耗时1.23秒左右
    print('Total time: {} seconds'.format(time() - start_time))

    bst_map.remove('they')
    print(bst_map.contains('they'))
    bst_map.setter('they', 100)
    print(bst_map.getter('they'))