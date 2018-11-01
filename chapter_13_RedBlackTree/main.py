from time import time

from chapter_07_Set_Map.bst_map import BSTMap
from chapter_13_RedBlackTree.rb_tree import RBTree


if __name__ == '__main__':
    words = ''
    with open('./chapter_07_Set_Map/shakespeare.txt', 'r') as f:
        words = f.read()
    words = words.split()

    start_time = time()
    bst_map = BSTMap()
    for word in words:
        if bst_map.contains(word):
            bst_map.setter(word, bst_map.getter(word) + 1)
        else:
            bst_map.add(word, 1)
    
    print('Total words: ', len(words))
    print('Unique words: ', bst_map.get_size())
    print('Contains word "they": ', bst_map.contains('they'))
    ## 耗时1.23秒左右
    print('BSTMap Total time: {} seconds'.format(time() - start_time))

    bst_map.remove('they')
    print(bst_map.contains('they'))
    bst_map.setter('they', 100)
    print(bst_map.getter('they'))

    print('*' * 20)

    start_time = time()
    rb_tree = RBTree()
    for word in words:
        if rb_tree.contains(word):
            rb_tree.setter(word, rb_tree.getter(word) + 1)
        else:
            rb_tree.add(word, 1)
    
    print('Total words: ', len(words))
    print('Unique words: ', rb_tree.get_size())
    print('Contains word "they": ', rb_tree.contains('they'))
    ## 耗时1.23秒左右
    print('RBTree Total time: {} seconds'.format(time() - start_time))

    rb_tree.remove('they')
    print(rb_tree.contains('they'))
    rb_tree.setter('they', 100)
    print(rb_tree.getter('they'))