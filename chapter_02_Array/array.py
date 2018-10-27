class Array:
    def __init__(self, capacity=10):
        self._data = [0] * capacity
        self._size = 0

    def get_size(self):
        return self._size

    def get_capacity(self):
        return len(self._data)

    def is_empty(self):
        return self._size == 0

    def add_last(self, e):
        self.add(self._size, e)

    def add_first(self, e):
        self.add(0, e)

    def add(self, index, e):
        """从后往前"""
        if self._size == len(self._data):
            raise ValueError('add failed. Array is full.')
        if not 0 <= index <= self._size:
            raise ValueError('add failed. Require index >= 0 and index <= array sise.')
        for i in range(self._size - 1, index - 1, -1):
            self._data[i + 1] = self._data[i]
        self._data[index] = e
        self._size += 1

    def get(self, index):
        if not 0 <= index < self._size:
            raise ValueError('get failed. Index is illegal.')
        return self._data[index]

    def set(self, index, e):
        if not 0 <= index < self._size:
            raise ValueError('set failed. Index is illegal.')
        self._data[index] = e

    def contains(self, e):
        for i in range(self._size):
            if self._data[i] == e:
                return True
        return False

    def find_index(self, e):
        for i in range(self._size):
            if self._data[i] == e:
                return i
        return -1

    def remove(self, index):
        if not 0 <= index < self._size:
            raise ValueError('remove failed. Index is illegal.')
        ret = self._data[index]
        for i in range(index + 1, self._size):
            self._data[i - 1] = self._data[i]
        self._size -= 1
        return ret

    def remove_first(self):
        return self.remove(0)

    def remove_last(self):
        return self.remove(self._size - 1)

    def remove_element(self, e):
        index = self.find_index(e)
        if index != -1:
            self.remove(index)

    def __str__(self):
        return str('<chapter_02_Array.array.Array>: {}'.format(self._data[:self._size]))

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    arr = Array()

    for i in range(8):
        arr.add_last(i)

    arr.add_last('zhe')

    arr.add_first(-1)
    print(arr)

    arr.remove_element(8)
    print(arr)

    arr.remove_element('zhe')
    print(arr)

