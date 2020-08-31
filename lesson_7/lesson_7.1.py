'''
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
[-100; 100). Выведите на экран исходный и отсортированный массивы.
'''

import random

def my_sort(my_array):
    arr = my_array.copy()
    for j in range(len(arr) - 1):
        for i in range(len(arr) - j - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

SIZE = 20
MIN_ITEM = -100
MAX_ITEM = 99
my_array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print('исх. массив: ', my_array)
print('рез. массив: ', my_sort(my_array))
print('исх. массив: ', my_array)



