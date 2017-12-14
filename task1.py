"""
    Home Work 2
    Pavel Shvarchov - 319270583
"""


def make_matrix(rows, cols, data):
    """
    creates a matrix
    :param rows: int
    :param cols: int
    :param data: list
    :return:dispatch list
    """
    size = rows * cols

    def get_row_count():
        return rows

    def get_col_count():
        return cols

    def get_row_data(row):
        if row >= rows:
            return None
        indexes = range(row * cols, (row + 1) * cols)
        return [data[i] for i in indexes]

    def get_col_data(col):
        if col >= cols:
            return None
        indexes = ((r * cols) + col for r in range(rows))
        return [data[i] for i in indexes]

    def get_data():
        return data

    def print_data():
        for i in range(size):
            print(data[i], end=' ')
            if (i + 1) % cols == 0:
                print()  # goes to next row

    def add(m2):
        if rows != n(m2) or cols != m(m2):
            return "cant add"
        data2 = matrix(m2)
        newdata = [data[i] + data2[i] for i in range(size + 1)]
        added = make_matrix(rows, cols, newdata)
        return added

    def transpose():
        data = []
        for c in range(cols):
            data += get_col_data(c)
        return make_matrix(cols, rows, data)

    def multiply(m2):
        if cols != n(m2):
            return "can't multiply"
        data = []
        for row in range(rows):
            row_data = get_row_data(row)
            for col in range(m(m2)):
                col_data = m2('get_col_data')(col)
                current_data = 0
                for i in range(cols):
                    current_data += row_data[i] * col_data[i]
                data.append(current_data)

        return make_matrix(rows, m(m2), data)

    def dispatch(msg):
        if msg == 'get_row_count':
            return get_row_count
        elif msg == 'get_col_count':
            return get_col_count
        elif msg == 'get_data':
            return get_data
        elif msg == 'print_data':
            return print_data
        elif msg == 'add':
            return add
        elif msg == 'get_row_data':
            return get_row_data
        elif msg == 'get_col_data':
            return get_col_data
        elif msg == 'transpose':
            return transpose
        elif msg == 'multiply':
            return multiply
        else:
            return

    return dispatch


def n(x):
    return x('get_row_count')()


def m(x):
    return x('get_col_count')()


def matrix(x):
    return x('get_data')()


def PrintMatrix(x):
    return x('print_data')()


def AddMatrix(x, y):
    return x('add')(y)


def InvertMatrix(x):
    return x('transpose')


def MulMatrix(x, y):
    return x('multiply')(y)


def print_rows(ma):
    for r in range(n(ma)):
        print("row {}: {}".format(r, ma('get_row_data')(r)))

def print_cols(ma):
    for c in range(m(ma)):
        print("col {}: {}".format(c, ma('get_col_data')(c)))


m1 = make_matrix(2, 3, [1, 2, 3, 4, 5, 6])
m2 = make_matrix(3, 2, [1, 2, 3, 4, 5, 6])


PrintMatrix(m1)
print('____')
PrintMatrix(m2)
print('____')
PrintMatrix(MulMatrix(m1, m2))
print("____")
