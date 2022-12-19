
def top10():
    n = 1

    while n <= 10:
        val = n * n
        n += 1
        yield val

value = top10()

print(value) # this will print object of generator.
print(value.__next__()) # we use __next__() method to print value from generator

for i in value:
    print(i)

