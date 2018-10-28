from chapter_02_Array.array import Array
from chapter_03_Stack_Queue.base import StackBase


class ArrayStack(StackBase):
    """使用自定义的Array实现"""
    def __init__(self, capacity=0):
        self._array = Array(capacity=capacity)

    def push(self, e):
        self._array.add_last(e)

    def pop(self):
        return self._array.remove_last()

    def peek(self):
        return self._array.get_last()

    def get_size(self):
        return self._array.get_size()

    def is_empty(self):
        return self._array.is_empty()

    def get_capacity(self):
        return self._array.get_capacity()

    def __str__(self):
        return str('<chapter_03_Stack_Queue.stack.ArrayStack> : {}'.format(self._array))

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':

    def is_valid(input_str):
        left_ = set(['(', '[', '{'])
        hash_ = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = ArrayStack()
        for ch in input_str:
            if ch in left_:
                stack.push(ch)
            else:
                if stack.get_size() == 0 or hash_[ch] != stack.pop():
                    return False
        return stack.is_empty()

    input_str1 = '[{(())}]'
    print(is_valid(input_str1))

    input_str1 = '[{(())})'
    print(is_valid(input_str1))
