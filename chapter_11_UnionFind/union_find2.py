from chapter_11_UnionFind.base import UF


# Second version - quick union
class UnionFind2(UF):
    def __init__(self, size):
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

    # O(h)
    def is_connected(self, p, q):
        return self._find(p) == self._find(q)

    # O(h)
    def union_elements(self, p, q):
        p_root = self._find(p)
        q_root = self._find(q)
        if p_root == q_root:
            return
        self._parent[p_root] = q_root