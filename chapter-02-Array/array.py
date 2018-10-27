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

if __name__ == '__main__':
    pass