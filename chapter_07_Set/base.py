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