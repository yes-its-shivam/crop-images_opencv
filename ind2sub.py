# linear index of a matrix to subscript index
# |00 01 02|    |01 02 03| 
# |04 05 06| -> |10 11 12|
# |07 08 09|    |20 21 22|

def ind2sub(linear_index, shape):
    subscript = []
    for dim_size in reversed(shape):
        subscript.append(linear_index % dim_size)
        linear_index //= dim_size
        s = ''
        for i in tuple(reversed(subscript)):
            s+=str(i)
    return s
