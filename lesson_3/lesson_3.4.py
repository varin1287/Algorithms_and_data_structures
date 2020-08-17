'''
Определить, какое число в массиве встречается чаще всего.
'''
import random

SIZE = 20
MIN_ITEM = -20
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

rez_num = array[0]
max_repit = 1
for i in range(len(array) - 1):
    my_repit = 1
    for k in range(i + 1, SIZE):
        if array[i] == array[k]:
            my_repit += 1
    if my_repit > max_repit:
        max_repit = my_repit
        rez_num = array[i]

if max_repit > 1:
    print(f'число {rez_num} встречается {max_repit } раз(-а) (чаще всего)' )
else:    print('числа не повторяются')

