A=[1,2,3,4]


def shuffle_array_value(a):
    b=a.copy()
    b[0],b[1]=b[1],b[0]
    return b

new=shuffle_array_value(A)
print(new)
print(A)