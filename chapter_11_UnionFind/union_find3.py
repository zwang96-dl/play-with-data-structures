from chapter_11_UnionFind.base import UF


# Third version - size opt
class UnionFind3(UF):
    def __init__(self, size):
        # sz[i]表示以i为根的集合中元素的个数
        self._sz = [1] * size
        self._parent = [i for i in range(size)]

    def get_size(self):
        return len(self._parent)

    def _find(self, p):
        if p < 0 or p >= len(self._parent):
            raise ValueError('p is out of bound.')
        # ONLY parent node points to itself
        while p != self._parent[p]:
            p = self._parent[p]
        return p

    def is_connected(self, p, q):
        return self._find(p) == self._find(q)

    def union_elements(self, p, q):
        p_root = self._find(p)
        q_root = self._find(q)
        if p_root == q_root:
            return
        # 连到高度比较低的节点上
        if self._sz[p_root] < self._sz[q_root]:
            self._parent[p_root] = q_root
            self._sz[q_root] += self._sz[p_root]
        else:
            self._parent[q_root] = p_root
            self._sz[p_root] += self._sz[q_root]