"""
    Home Work 2
    Pavel Shvarchov - 319270583
"""


data=" 1,1 ,, 100,3 , 5,5,5 ,, 1,2,3 "

def enumerate(data):
    return map(lambda i:None if i=='' else float(i) if '.' in i else int(i),data.split(','))

def clean(data,min_val,max_val):
    return filter(lambda i:i==None or (min_val<=i and i<=max_val),data)

# def complete_missing_values(data):
#     return map(lambda a,b,c:)
# print(data)
# print(list(enumerate(data)))
# print(list(clean(enumerate(data),1,20)))
b=0
print(list(filter(lambda a,b:a,[1,2,3,4,5,6,7,8,9])))