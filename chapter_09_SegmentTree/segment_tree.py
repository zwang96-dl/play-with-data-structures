class SegmentTree:
    def __init__(self, arr, merger):
        """线段树相当于将数组用一棵树重新表示"""
        if not isinstance(arr, list) or not arr or not merger:
            raise ValueError('Can not initialize empty array.')
        self._data = arr[:]
        self._tree = [None] * 4 * len(arr)
        self._merger = merger
        self._build_segment_tree(tree_index=0, l=0, r=len(self._data) - 1)

    def get_size(self):
        return len(self._data)

    def get(self, index):
        if index < 0 or index >= len(self._data):
            raise ValueError('Index is ieelgal.')
        return self._data[index]

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    # 在tree_index位置创建表示区间[l...r]的线段树
    # 左右的端点l, r
    def _build_segment_tree(self, tree_index, l, r):
        if l == r:
            self._tree[tree_index] = self._data[l]
            return
        left_tree_index = self._left_child(tree_index)
        right_tree_index = self._right_child(tree_index)
        mid = l + (r - l) // 2
        self._build_segment_tree(left_tree_index, l, mid)
        self._build_segment_tree(right_tree_index, mid + 1, r)
        self._tree[tree_index] = self._merger(
            self._tree[left_tree_index],
            self._tree[right_tree_index],
        )

    def __str__(self):
        res = []
        res.append('[')
        for i in range(len(self._tree)):
            res.append(str(self._tree[i]))
            if i != len(self._tree) - 1:
                res.append(', ')
        res.append(']')
        return '<chapter_08_SegmentTree.segment_tree.SegmentTree>: ' + ''.join(res)

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    sum_merger = lambda a, b: a + b
    seg_tree = SegmentTree(arr=nums, merger=sum_merger)
    print(seg_tree)