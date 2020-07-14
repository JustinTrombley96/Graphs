ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
oldest_parent = []
values = []

def answer(ancestors):
    for key, value in ancestors:
            # print(key, value)
            values.append(value)
            # print(values)
            if key not in values:
                # print(key)
                print('Values List: ', values)
                oldest_parent.append(key)
    print('Oldest Parent: ', oldest_parent)
    return oldest_parent


answer(ancestors)