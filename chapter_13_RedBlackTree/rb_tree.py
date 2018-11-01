RED = True
BLACK = False

class RBTree:
    class _Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            # new node must be a leaf node and merge to the current leaf node
            # so it is red by default
            self.color = RED

    def __init__(self):
        self._root = None
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _is_red(self, node):
        if not node:
            # empty node is black
            return BLACK
        return node.color

    #       node                            x
    #       /  \          左旋转            / \
    #      T1   x     ------------>      node T3
    #          / \                       /  \
    #         T2  T3                    T1   T2
    def _left_rotate(self, node):
        x = node.right
        node.right = x.left
        x.left = node
        x.color = node.color
        node.color = RED
        return x

    #       node                            x
    #       /  \          右旋转            / \
    #      x    T2    ------------->      y node
    #     / \                               /  \
    #    y  T1                             T1   T2
    def _right_rotate(self, node):
        x = node.left
        node.left = x.right
        x.right = node
        x.color = node.color
        node.color = RED
        return x

    def _flip_colors(self, node):
        node.color = RED
        node.left.color = BLACK
        node.right.color = BLACK

    # 向红黑树种添加新的元素
    def add(self, key, value):
        self._root = self._add(self._root, key, value)
        self._root.color = BLACK

    # 向以node为根的红黑树中添加新的元素
    # 返回插入新节点后红黑树的根
    def _add(self, node, key, value):
        if not node:
            self._size += 1
            return self._Node(key, value) # 默认插入红色节点
        if key < node.key:
            node.left = self._add(node.left, key, value)
        elif key > node.key:
            node.right = self._add(node.right, key, value)
        else:
            node.value = value
        # 左旋转 -> 右旋转 -> 颜色翻转
        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._left_rotate(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._right_rotate(node)
        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_colors(node)
        return node

    def _get_node(self, node, key):
        if not node:
            return
        if key == node.key:
            return node
        elif node.key > key:
            return self._get_node(node.left, key)
        else:
            return self._get_node(node.right, key)

    def contains(self, key):
        """以root为根有没有key"""
        return self._get_node(self._root, key) is not None

    def getter(self, key):
        node = self._get_node(self._root, key)
        return node.value if node else None

    def setter(self, key, value):
        node = self._get_node(self._root, key)
        if not node:
            raise ValueError('{} doesn\'t exist!'.format(str(key)))
        node.value = value

    def _minimum(self, node):
        if not node.left:
            return node
        return self._minimum(node.left)

    # 删除掉以node为根的BST中的最小节点
    # 返回删除节点后新的BST的根
    def _remove_min(self, node):
        # 递归终止
        if not node.left:
            right_node = node.right
            node.right = None
            self._size -= 1
            return right_node
        node.left = self._remove_min(node.left)
        return node

    def remove(self, key):
        node = self._get_node(self._root, key)
        if not node:
            self._root = self._remove(self._root, key)
            return node.value

    # 删除以node为根的BST中值为e的节点，递归算法
    # 返回删除节点后的新的BST的根
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
            successor = self._minimum(node.right)
            successor.right = self._remove_min(node.right)
            successor.left = node.left
            node.left = node.right = None
            return successor

    def _generate_depth_string(self, depth):
        res = ''
        for i in range(depth):
            res += '--'
        return res

    def _generate_RBTree_string(self, node, depth, res):
        if not node:
            res.append(self._generate_depth_string(depth) + 'None\n')
            return
        res.append(self._generate_depth_string(depth) + str(node.key) + '\n')
        self._generate_RBTree_string(node.left, depth + 1, res)
        self._generate_RBTree_string(node.right, depth + 1, res)

    def __str__(self):
        res = []
        self._generate_RBTree_string(self._root, 0, res)
        return '<chapter_13_RBTree.rb_tree.RBTree>:\n' + ''.join(res)

    def __repr__(self):
        return self.__str__()