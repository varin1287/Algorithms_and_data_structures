'''
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
'''

MIN_ITEM = 2
MAX_ITEM = 99
FIND_MIN = 2
FIND_MAX = 9

rez = [0] * (FIND_MAX - FIND_MIN + 1)

for i in range(MIN_ITEM, MAX_ITEM + 1):
    for j in range(FIND_MIN, FIND_MAX + 1):
        if i % j == 0:
            rez[j - FIND_MIN] += 1

for j in range(FIND_MIN, FIND_MAX + 1):
    print(f'{j} - {rez[j - FIND_MIN]}')






















