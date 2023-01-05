
def add_to_tup(tuple, element):
    for i in tuple:
        if isinstance(i, list):
            i.append(element)

    print(tuple)


tup = (1, 2, 3, [0, 0, 0])

element = 5


add_to_tup(tup, element)