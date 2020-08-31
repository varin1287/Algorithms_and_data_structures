'''
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану
Использована шейкерная сортировка
'''


import random

def my_mediana(my_array):
    arr = my_array.copy()
    left = 0
    right = len(arr) - 1
    while left <= right:
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1

        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        left += 1
    print('упорядоченный массив: ', arr)
    return arr[len(arr) // 2]

m = int(input('введите натуральное m: '))

size = 2 * m + 1
MIN_ITEM = 0
MAX_ITEM = 10
my_array = [round(random.randint(MIN_ITEM, MAX_ITEM), 2) for _ in range(size)]

print('исходный массив: ', my_array)
print('медиана', my_mediana(my_array))

