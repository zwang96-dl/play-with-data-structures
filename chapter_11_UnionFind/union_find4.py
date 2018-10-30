from chapter_11_UnionFind.base import UF


# Fourth version - rank opt
class UnionFind4(UF):
    def __init__(self, size):
        # rank[i]表示以i为根的树的层数(深度)
        self._rank = [1] * size
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
        # 根据两个元素所在树的rank不同判断合并方向
        # 将rank低的集合合并到rank高的集合上(merge)
        if self._rank[p_root] < self._rank[q_root]:
            self._parent[p_root] = q_root
        elif self._rank[p_root] > self._rank[q_root]:
            self._parent[q_root] = p_root
        else:
            self._parent[q_root] = p_root
            # 想象两个点（rank 1）的合并，肯定结果是一个是另个一个的孩子
            # 所以rank会加1
            self._rank[p_root] += 1 