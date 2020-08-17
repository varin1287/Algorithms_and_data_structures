'''
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
'''
import random

SIZE = 10
MIN_ITEM = -20
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

my_max = array[0]
pos = 0
for i in range(1, len(array)):
    if array[i] < 0 and array[i] > my_max:
        my_max = array[i]
        pos = i
if my_max < 0:
    print(f'максимальный отрицательный элемент {my_max} его позиция {pos}')
else:
    print('в массиве нет отрицательных чисел')





