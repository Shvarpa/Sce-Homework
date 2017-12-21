"""
    Home Work 2
    Pavel Shvarchov - 319270583
"""



def make_sequence(data, iterate=False):
    size = 0
    if iterate:
        current = 0

    def update_size():
        nonlocal size
        size = 0
        for _ in data:
            size += 1

    update_size()

    def all_filter(func=lambda x: True):
        return tuple(x for x in data if func(x))

    def return_filter(func=lambda x: True):
        return make_sequence(tuple(x for x in data if func(x)), True)

    def next():
        nonlocal current
        if iterate == False:
            return 'no filter initiated'
        print(data[current])
        current = (current + 1) % size

    def reverse():
        nonlocal current, size
        if iterate == False:
            return tuple(data[(size - 1) - i] for i in range(size))
        print(data[current])
        current = (current - 1) % size

    def extend(extra):
        nonlocal data
        data_class = type(data)
        data = data_class(tuple(data) + tuple(extra))
        update_size()

    def clear():
        all_filter(lambda x: False)

    return {'all_filter': all_filter,
            'return_filter': return_filter,
            'next': next,
            'reverse': reverse,
            'extend': extend,
            'clear': clear,
            }

def example():
    s1 = make_sequence((1, 2, 3, 4, 5))
    print(s1['all_filter'](lambda x: x % 2 == 0))
    p1 = s1['return_filter'](lambda x: x < 4)
    p1['next']()
    for _ in range(5):
        p1['next']()
    for _ in range(3):
        p1['reverse']()
    s1['extend'](s1['all_filter'](lambda x: x % 2 != 0))
    print(s1['all_filter'](lambda x: x > 2))
    print(s1['all_filter']())
    print((make_sequence(s1['reverse']()))['all_filter'](lambda x: x < 4))


if __name__ == '__main__':
    example()
