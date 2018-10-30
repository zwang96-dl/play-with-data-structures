class Trie:
    class _Node:
        def __init__(self, is_word=False):
            self.is_word = is_word
            self.next = [None] * 26

    def __init__(self):
        self._root = self._Node()
        # Trie中有多少个单词
        self._size = 0

    def get_size(self):
        return self._size

    def add(self, word):
        curr = self._root
        for ch in word:
            index = ord(ch.lower()) - ord('a')
            if curr.next[index] is None:
                curr.next[index] = self._Node()
            curr = curr.next[index]
        if curr.is_word == False:
            curr.is_word = True
            self._size += 1

    def contains(self, word):
        curr = self._root
        for ch in word:
            index = ord(ch.lower()) - ord('a')
            if curr.next[index] is None:
                return False
            curr = curr.next[index]
        return curr.is_word

    def is_prefix(self, prefix):
        curr = self._root
        for ch in prefix:
            index = ord(ch.lower()) - ord('a')
            if curr.next[index] is None:
                return False
            curr = curr.next[index]
        return True


if __name__ == '__main__':
    trie = Trie()
    words = ['panda', 'pandas', 'apple', 'app', 'banana']
    for word in words:
        trie.add(word)

    print('panda', trie.contains('panda'))
    print('pan', trie.contains('pan'))
    print('pana', trie.is_prefix('pana'))
    print('zzz', trie.contains('zzz'))
