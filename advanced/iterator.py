"""
 Reference : https://www.scaler.com/topics/python/iterators-in-python/

 - In python everything is object including variables, functions, lists, tuples, set, etc.
 - There are some objects which are iterable, which means we can traverse over them and
    they will return their member value one by one. e.g  List, Tuple, Dictionary, Set, String.
 - Iterators are implemented using two special methods in Python which are iter() and next().
    They are collectively called iterator protocol.

 - The iter() method is used to create the iterator over the iterable object.
 - The next() method returns the next item from the iterator.

How to Make Custom Iterators in Python?
 - For making our own iterator we have to use two dunder/magic methods provided by Python.
 - __iter__() should return the iterator object. If required, some initialization can be performed.
 - __next__() should return the next item in the sequence. On reaching the end it should raise
    StopIteration.
"""
nums = [1,2,5,7,8]

it = iter(nums)

print(it.__next__())
print(it.__next__())

class Top10:
    def __init__(self):
        self.num = 1

    def __iter__(self): # need object of iterator
        return self

    def __next__(self):# to get next num.
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
value = Top10()

for i in value:
    print(i)