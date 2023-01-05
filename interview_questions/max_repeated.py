
# Using Counter and most common function
from collections import Counter
def max_repeated(lis):
    ct = Counter(lis)
    print(ct.most_common()[0][0])


# Using iterative approach and count function on list
def max_repeated2(lis):
    counter = 0
    num = lis[0]

    for i in lis:
        current_freq = lis.count(i)
        if current_freq > counter:
            counter = current_freq
            num = i
    print(num)


lis = [1, 1, 1, 2, 2, 2, 2, 3, 4,5]

max_repeated(lis)
max_repeated2(lis)