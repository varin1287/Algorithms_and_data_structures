'''
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
'''
import random

def my_func(left_list, right_list):
    res = []
    i = 0
    j = 0
    while len(left_list) > i and len(right_list) > j:
        if left_list[i] < right_list[j]:
            res.append(left_list[i])
            i += 1
        else:
            res.append(right_list[j])
            j += 1

    res.extend(right_list[j:])
    res.extend(left_list[i:])
    return res



def my_sort(arr):
    if len(arr) == 1:
        return arr
    spam = len(arr) // 2
    left_list = my_sort([arr[i] for i in range(spam)])
    right_list = my_sort([arr[i] for i in range(spam, len(arr))])
    return my_func(left_list, right_list)


SIZE = 15
MIN_ITEM = 0
MAX_ITEM = 49
my_array = [round(random.uniform(MIN_ITEM, MAX_ITEM), 2) for _ in range(SIZE)]


copy_array = my_array.copy()
print('рез. массив: ', my_sort(copy_array))
print('исх. массив: ', my_array)

