import numpy as np

new_array = np.array([2,4,6,8])

def array_num(arr):
    arr_sum = 0
    for num in arr:
        arr_sum = arr_sum + num
    return arr_sum

print(array_num(new_array))

