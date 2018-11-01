from time import time

from chapter_14_HashTable.hash_table import HashTable


if __name__ == '__main__':
    words = ''
    with open('./chapter_07_Set_Map/shakespeare.txt', 'r') as f:
        words = f.read()
    words = words.split()

    start_time = time()
    hashtable = HashTable(M=131071)
    for word in words:
        if hashtable.contains(word):
            hashtable.setter(word, hashtable.getter(word) + 1)
        else:
            hashtable.add(word, 1)
    
    print('Total words: ', len(words))
    print('Unique words: ', hashtable.get_size())
    print('Contains word "they": ', hashtable.contains('they'))
    ## 耗时1.23秒左右
    print('HashTable Total time: {} seconds'.format(time() - start_time))