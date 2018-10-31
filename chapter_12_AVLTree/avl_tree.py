class AVLTree:
    class _Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = None
            self.right = None
            self.height = 1

    def __init__(self):
        self._root = None
        self._size = 0

    def get_size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def is_banlanced(self):
        return self._is_banlanced(self._root)

    def _is_banlanced(self, node):
        if not node:
            return True
        banlanced_factor = self._get_banlance_factor(node)
        if abs(banlanced_factor) > 1:
            return False
        return self._is_banlanced(node.left) and self._is_banlanced(node.right)

    def is_bst(self):
        keys = []
        self._in_order(self._root, keys)
        for i in range(1, len(keys)):
            if keys[i - 1] > keys[i]:
                return False
        return True

    def _in_order(self, keys):
        if not node:
            return
        self._in_order(node.left, keys)
        keys.append(node.key)
        self._in_order(node.right, keys)

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_banlance_factor(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

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
        # 需要更新height
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        banlance_factor = self._get_banlance_factor(node)
        # 左边高 LL
        if banlance_factor > 1 and self._get_banlance_factor(node.left) >= 0:
            return self._right_rotate(node)
        # 右边高 RR
        if banlance_factor < -1 and self._get_banlance_factor(node.right) <= 0:
            return self._left_rotate(node)
        # LR
        if banlance_factor > 1 and self._get_banlance_factor(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
        # RL
        if banlance_factor < -1 and self._get_banlance_factor(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)
        return node

    def _right_rotate(self, y):
        """
        对节点y进行向右旋转操作，返回旋转后的新的根节点x
                y                                 x
               / \                               / \
              x   T4      向右旋转 (y)           z    y
             / \        -------------->       / \   / \
            z   T3                           T1 T2 T3  T4
           / \
          T1  T2
        """
        x = y.left
        T3 = x.right
        x.right = y
        y.left = T3
        # 更新height
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        return x

    def _left_rotate(self, y):
        """
        对节点y进行向左旋转操作，返回旋转后的新的根节点x
             y                                 x
            / \                               / \
           T1  x      向右旋转 (y)            y    z
              / \     -------------->      / \   / \
             T2  z                        T1 T2 T3  T4
                / \
               T1 T2
        """
        x = y.right
        T2 = x.left
        x.left = y
        y.right = T2
        # 更新height
        y.height = max(self._get_height(y.left), self._get_height(y.right)) + 1
        x.height = max(self._get_height(x.left), self._get_height(x.right)) + 1
        return x

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

    def _remove(self, node, key):
        # 递归终止
        if not node:
            return
        # 递归条件
        if node.key > key:
            node.left = self._remove(node.left, key)
            ret_node = node
        elif node.key < key:
            node.right = self._remove(node.right, key)
            ret_node = node
        else: # node.key == key
            if not node.left:
                right_node = node.right
                node.right = None
                self._size -= 1
                ret_node = right_node
            elif node.right:
                left_node = node.left
                node.left = None
                self._size -= 1
                ret_node = left_node
            else:
                # 如果左右子树均不为空
                # 找到比待删除节点大的最小节点，即待删除节点右子树的最小节点
                # 用这个节点顶替待删除节点的位置
                successor = self.minimum(node.right)
                successor.right = self._remove(node.right, successor.key)
                successor.left = node.left
                node.left = node.right = None
                ret_node = successor
        if not ret_node:
            return
        # 需要更新height
        ret_node.height = 1 + max(
            self._get_height(ret_node.left),
            self._get_height(ret_node.right),
        )
        banlance_factor = self._get_banlance_factor(ret_node)
        # 左边高 LL
        if banlance_factor > 1 and self._get_banlance_factor(ret_node.left) >= 0:
            return self._right_rotate(ret_node)
        # 右边高 RR
        if banlance_factor < -1 and self._get_banlance_factor(ret_node.right) <= 0:
            return self._left_rotate(ret_node)
        # LR
        if banlance_factor > 1 and self._get_banlance_factor(ret_node.left) < 0:
            ret_node.left = self._left_rotate(ret_node.left)
            return self._right_rotate(ret_node)
        # RL
        if banlance_factor < -1 and self._get_banlance_factor(ret_node.right) > 0:
            ret_node.right = self._right_rotate(ret_node.right)
            return self._left_rotate(ret_node)
        return ret_node

    def minimum(self):
        if self.is_empty():
            raise ValueError('AVLTree is empty!')
        self._minimum(self._root)

    def _minimum(self, node):
        if not node.left:
            return node
        return self._minimum(node.left)

    def _remove_min(self, node):
        # 递归终止
        if not node.left:
            right_node = node.right
            node.right = None
            self._size -= 1
            return right_node
        node.left = self._remove_min(node.left)
        return node