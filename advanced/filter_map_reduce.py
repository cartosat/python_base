from functools import reduce
nums = [1,2,3,4,5,6,7,8,9,10]

#Filter --> filtering even nums
#takes function and itterable.

evens = list(filter(lambda x: x%2==0, nums))
print("filter :- ", evens)

double = list(map(lambda x: x*2, evens))
print("map :- ", double)

sum_ = reduce(lambda a,b :a+b, double)
print("reduce :- ", sum_)
