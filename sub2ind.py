#subscript index of a matrix to linear index
# |00 01 02|    |01 02 03|
# |10 11 12| -> |04 05 06|
# |20 21 22|    |07 08 09|
import numpy as np

def sub2ind(subs, shape):
    index = 0
    for i in range(len(subs)):
        if subs[i] < 0 or subs[i] >= shape[i]:
            raise IndexError("Index out of bounds")
        else:
            index += subs[i] * np.prod(shape[i+1:])
    return int(index)