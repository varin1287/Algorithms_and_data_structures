# Урок 2 задание 3
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

import random
import timeit
import cProfile
import sys

sys.setrecursionlimit(10000000)  # Помню про нехватку памяти, но для тестирования рекурсии использовал ( у меня памяти меньше чем у заказчика т.е. у вас)


def my_func_1(n, result=0):
    if n == 0:
        return result
    else:
        return my_func_1(n // 10, result * 10 + n % 10)


def my_func_2(n):
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n = n // 10
    return result


def my_func_3(n):
    result = ''
    n = str(n)
    for i in n:
        result = i + result
    return result


def my_func_4(n):
    n = str(n)
    result = n[::-1]
    return result


def my_num(size):
    return random.randint(10 ** (size - 1), 10 ** size - 1)


FIRST_SIZE = 300  # больше 300 превышен стек, в видео было как ограничить его в функции, но с ходу не нашел. Потом пересмотрю.
n1 = my_num(FIRST_SIZE)
n2 = my_num(FIRST_SIZE * 2)
n3 = my_num(FIRST_SIZE * 4)
n4 = my_num(FIRST_SIZE * 8)
n5 = my_num(FIRST_SIZE * 16)

'''
print('исходное число: ', n)
print(f'новое число: {my_func_1(n)}')
print(f'новое число: {my_func_2(n)}')
print(f'новое число: {my_func_3(n)}')
print(f'новое число: {my_func_4(n)}')
'''

print('вариант 1')
print(timeit.timeit('my_func_1(n1)', number=1000, globals=globals()))  # 0.5686027
print(timeit.timeit('my_func_1(n2)', number=1000, globals=globals()))  # 2.2500080999999996
print(timeit.timeit('my_func_1(n3)', number=1000, globals=globals()))  # 7.065450700000001
print(timeit.timeit('my_func_1(n4)', number=1000, globals=globals()))  # 29.715726600000004
print(timeit.timeit('my_func_1(n5)', number=1000, globals=globals()))  # 109.2376732

cProfile.run('my_func_1(n1)')  # 301/1    0.001    0.000    0.001    0.001 test.py:10(my_func_1)
cProfile.run('my_func_1(n2)')  # 601/1    0.004    0.000    0.004    0.004 test.py:10(my_func_1)
cProfile.run('my_func_1(n3)')  # 1201/1    0.008    0.000    0.008    0.008 test.py:10(my_func_1)
cProfile.run('my_func_1(n4)')  # 2401/1    0.029    0.000    0.029    0.029 test.py:10(my_func_1)
cProfile.run('my_func_1(n5)')  # 4801/1    0.114    0.000    0.114    0.114 test.py:10(my_func_1)

print('вариант 2')
print(timeit.timeit('my_func_2(n1)', number=1000, globals=globals()))  # 0.4763881000000083
print(timeit.timeit('my_func_2(n2)', number=1000, globals=globals()))  # 1.8998358000000053
print(timeit.timeit('my_func_2(n3)', number=1000, globals=globals()))  # 6.7856061999999895
print(timeit.timeit('my_func_2(n4)', number=1000, globals=globals()))  # 25.15486439999998
print(timeit.timeit('my_func_2(n5)', number=1000, globals=globals()))  # 89.5421771

cProfile.run('my_func_2(n1)')  # 1    0.000    0.000    0.000    0.000 test.py:17(my_func_2)
cProfile.run('my_func_2(n2)')  # 1    0.001    0.001    0.001    0.001 test.py:17(my_func_2)
cProfile.run('my_func_2(n3)')  # 1    0.004    0.004    0.004    0.004 test.py:17(my_func_2)
cProfile.run('my_func_2(n4)')  # 1    0.015    0.015    0.015    0.015 test.py:17(my_func_2)
cProfile.run('my_func_2(n5)')  # 1    1    0.066    0.066    0.066    0.066 test.py:17(my_func_2)

print('вариант 3')
print(timeit.timeit('my_func_3(n1)', number=1000, globals=globals()))  # 0.07270369999997683
print(timeit.timeit('my_func_3(n2)', number=1000, globals=globals()))  # 0.19007560000000012
print(timeit.timeit('my_func_3(n3)', number=1000, globals=globals()))  # 0.4872732999999698
print(timeit.timeit('my_func_3(n4)', number=1000, globals=globals()))  # 1.516344600000025
print(timeit.timeit('my_func_3(n5)', number=1000, globals=globals()))  # 4.32771409999998

cProfile.run('my_func_3(n1)')  # 1    0.000    0.000    0.000    0.000 test.py:25(my_func_3)
cProfile.run('my_func_3(n2)')  # 1    0.000    0.000    0.000    0.000 test.py:25(my_func_3)
cProfile.run('my_func_3(n3)')  # 1    0.001    0.001    0.001    0.001 test.py:25(my_func_3)
cProfile.run('my_func_3(n4)')  # 1    0.002    0.002    0.002    0.002 test.py:25(my_func_3)
cProfile.run('my_func_3(n5)')  # 1    0.004    0.004    0.004    0.004 test.py:25(my_func_3)

print('вариант 4')
print(timeit.timeit('my_func_4(n1)', number=1000, globals=globals()))  # 0.018461999999999534
print(timeit.timeit('my_func_4(n2)', number=1000, globals=globals()))  # 0.056597299999964434
print(timeit.timeit('my_func_4(n3)', number=1000, globals=globals()))  # 0.2156853000000183
print(timeit.timeit('my_func_4(n4)', number=1000, globals=globals()))  # 0.6524503999999638
print(timeit.timeit('my_func_4(n5)', number=1000, globals=globals()))  # 2.286636099999953

cProfile.run('my_func_4(n1)')  # 1    0.000    0.000    0.000    0.000 test.py:33(my_func_4)
cProfile.run('my_func_4(n2)')  # 1    0.000    0.000    0.000    0.000 test.py:33(my_func_4)
cProfile.run('my_func_4(n3)')  # 1    0.000    0.000    0.000    0.000 test.py:33(my_func_4)
cProfile.run('my_func_4(n4)')  # 1    0.000    0.000    0.000    0.000 test.py:33(my_func_4)
cProfile.run('my_func_4(n5)')  # 1    0.002    0.002    0.002    0.002 test.py:33(my_func_4)

'''
Итог: 
1. - рекурсия самый  медленный вариант, увеличение времени работы линейнейное (увеличение в 4 раза) 
   - из всех вариантов самый долгий
   - нужен пример где рекурсия будет эфективнее цикла

2. -в разборе дз назван класическим вариантом   
   - по сравнению с 3 и 4, долгий вариант
   - немного быстрее рекурсии 

3. - в разборе дз сказанно, что будет много раз перезаписывать переменные, поэтому займет много памяти и 
    будет долго выполняться (вебинар 3, около 20 мин), однако выполняется быстрее рекурсии и "класического" варианта
   - предпологаю, что он второй по скорости т.к. меньше вычеслений по сравнению с вар 2, но большая разница в скорости не понятна

4. - ожидаемо самый быстрый

N (кол-во цифр в числе) для первого измерения 300 дяльше удваивается

'''





