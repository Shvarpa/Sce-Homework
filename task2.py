"""
    Home Work 2
    Pavel Shvarchov - 319270583
"""
from functools import reduce


def enumerate(data):
    return list(map(lambda i: None if i == '' else float(i) if '.' in i else int(i), data.split(',')))


def clean(data, min_val, max_val):
    return list(filter(lambda i: i == None or (min_val <= i and i <= max_val), data))


def complete_missing_values(data):
    data = list(data)
    size = reduce(lambda x, y: x + 1, data, 0)
    return list(map(lambda x: (data[x - 1] + data[x + 1]) / 2 if data[x] == None else data[x], range(size)))


def data_preprocessing_histogram(data, min_val, max_val):
    data = list(complete_missing_values(clean(enumerate(data), min_val, max_val)))
    size = reduce(lambda x, y: x + 1, data, 0)
    reduced=filter(lambda i:not data[i+1:].__contains__(data[i]), range(size))
    reduced = list(map(lambda i:data[i],reduced))
    reduced_size=reduce(lambda x, y: x + 1, reduced, 0)
    counts=list(map(lambda x:reduce(lambda _,y:_+(1 if y==x else 0),data,0),reduced))
    return list(zip(reduced,counts))

def data_preprocessing_range(data,min_val,max_val):
    data = list(complete_missing_values(clean(enumerate(data), min_val, max_val)))
    min=reduce(lambda curr,x:x if x<curr else curr,data[1:],data[0])
    max=reduce(lambda curr,x:x if x>curr else curr,data[1:],data[0])
    size = reduce(lambda x, y: x + 1, data, 0)
    avg=reduce(lambda curr,x:curr+x,data,0)/size
    return (min,avg,max)


def example():
    data = "1,1,,100,3, 5,5,5,,1,2,3"
    min_val, max_val = 0, 10
    print(enumerate(data))
    print(clean(enumerate(data),min_val,max_val))
    print(complete_missing_values(clean(enumerate(data),min_val,max_val)))
    print(data_preprocessing_histogram(data, min_val, max_val))
    print(data_preprocessing_range(data, min_val, max_val))

if __name__=='__main__':
    example()