class SetBase:
    def add(self, e):
        raise NotImplementedError

    def remove(self, e):
        raise NotImplementedError

    def contains(self, e):
        raise NotImplementedError

    def get_size(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError


class MapBase:
    def add(self, key, value):
        raise NotImplementedError

    def remove(self, key):
        raise NotImplementedError

    def contains(self, key):
        raise NotImplementedError

    def getter(self, key):
        raise NotImplementedError

    def setter(self, key, value):
        raise NotImplementedError

    def get_size(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError