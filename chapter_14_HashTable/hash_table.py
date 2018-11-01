from collections import defaultdict


_UPPER_TOL = 10
_LOWER_TOL = 2
_INIT_CAPACITY = 7

class HashTable:
    def __init__(self, M=_INIT_CAPACITY):
        self._M = M
        self._hashtable = [defaultdict() for _ in range(M)]
        self._size = 0

    def _hash(self, key):
        return hash(key) % 0x7fffffff % self._M

    def get_size(self):
        return self._size

    def add(self, key, value):
        _map = self._hashtable[self._hash(key)]
        if key in _map:
            _map[key] = value
        else:
            _map[key] = value
            self._size += 1
            if self._size >= _UPPER_TOL * self._M:
                self._resize(2 * self._M)

    def remove(self, key):
        ret = None
        _map = self._hashtable[self._hash(key)]
        if key in _map:
            ret = _map.pop(key)
            self._size -= 1
            if self._size < _LOWER_TOL * self._M and \
                self._M // 2 >= _INIT_CAPACITY:
                self._resize(self._M // 2)
        return ret

    def setter(self, key, value):
        _map = self._hashtable[self._hash(key)]
        if key not in _map:
            raise ValueError('{} doesn\'t exist!'.format(key))
        _map[key] = value

    def contains(self, key):
        return key in self._hashtable[self._hash(key)]

    def getter(self, key):
        # 因为self._hashtable[self._hash(key)]是一个defaultdict
        # 所以index访问时安全的，默认为None
        return self._hashtable[self._hash(key)][key]

    def _resize(self, new_M):
        new_hashtable = [defaultdict() for _ in range(new_M)]
        old_M = self._M
        self._M = new_M
        for i in range(old_M):
            _map = self._hashtable[i]
            for key, value in _map.items():
                new_hashtable[self._hash(key)][key] = value
        self._hashtable = new_hashtable