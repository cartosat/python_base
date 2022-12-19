
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