import itertools
'''
count
cycle
repeat
'''
counter = itertools.count(start=0, step=2) #gives infinite number with step and starting from start arg.

for i in counter:
    if i <= 10:
        print(i)
    else:
        break

#Cycle --> Repeatedly print all values from given iterator.

cycler = itertools.cycle((1,2,3,4,5))

count = 0
for i in cycler:
    if count == 10:
        break
    else:
        print(i)
    count+=1

# Repeat --> This iterator repeatedly prints the passed value an infinite number of times.

repeater = itertools.repeat((11, 12), 5)

print("======Repeat======")
for i in repeater:
    print(i)

'''
Difference between cycle and repeat
    -> cycle prints each element of iterator.
    -> repeat repeats the whole iterator.

'''
