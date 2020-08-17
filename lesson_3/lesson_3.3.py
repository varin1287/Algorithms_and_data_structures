'''
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
'''
import random

SIZE = 10
MIN_ITEM = -20
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

print(f'исходный массив\n {array}')
my_min, my_max = 0, 0
my_flag = False

for i in range(1,len(array)):
    if array[i] > array[my_max]:
        my_max = i
    elif array[i] < array[my_min]:
        my_min = i

print(f'максимум и минимум {array[my_max]}, {array[my_min]}')
array[my_min], array[my_max] = array[my_max], array[my_min]
print(f'результат\n {array}')








