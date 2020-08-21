'''
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
'''

import math
import timeit
import cProfile

def my_funk(i):
    n = 1
    num = 2
    while True:
        if n == i:
            return num
        num += 1
        for j in range(2, num):
            if num % j == 0:
                n -= 1
                break
        n += 1


def sieve_erot(num_of_elem):
    n = math.ceil(2 * num_of_elem * math.log(num_of_elem, math.e))    # Функция распределения простых чисел
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    return res[num_of_elem - 1]

i = 7
#print(my_funk(i))
#print(sieve_erot(i))

print('вариант без решета')
print(timeit.timeit('my_funk(10)', number=1000, globals=globals()))  # 0.0299887
print(timeit.timeit('my_funk(20)', number=1000, globals=globals()))  # 0.11918759999999999
print(timeit.timeit('my_funk(40)', number=1000, globals=globals()))  # 0.5985052
print(timeit.timeit('my_funk(80)', number=1000, globals=globals()))  # 1.4605848999999997
print(timeit.timeit('my_funk(160)', number=1000, globals=globals()))  # 6.5278223

cProfile.run('my_funk(10)')  # 1    0.000    0.000    0.000    0.000 lesson_4.2.py:10(my_funk)
cProfile.run('my_funk(20)')  # 1    0.000    0.000    0.000    0.000 lesson_4.2.py:10(my_funk)
cProfile.run('my_funk(40)')  # 1    0.000    0.000    0.000    0.000 lesson_4.2.py:10(my_funk)
cProfile.run('my_funk(80)')  # 1    0.002    0.002    0.002    0.002 lesson_4.2.py:10(my_funk)
cProfile.run('my_funk(160)') # 1    0.009    0.009    0.009    0.009 lesson_4.2.py:10(my_funk)


print('вариант с решетом')
print(timeit.timeit('sieve_erot(10)', number=1000, globals=globals()))  # 0.021438799999998537
print(timeit.timeit('sieve_erot(20)', number=1000, globals=globals()))  # 0.04722190000000026
print(timeit.timeit('sieve_erot(40)', number=1000, globals=globals()))  # 0.15329060000000005
print(timeit.timeit('sieve_erot(80)', number=1000, globals=globals()))  # 0.36946939999999984
print(timeit.timeit('sieve_erot(160)', number=1000, globals=globals()))  # 0.9123225999999995

cProfile.run('sieve_erot(10)')
cProfile.run('sieve_erot(20)')
cProfile.run('sieve_erot(40)')
cProfile.run('sieve_erot(80)')
cProfile.run('sieve_erot(160)')
'''
без решета
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.009    0.009 <string>:1(<module>)
        1    0.009    0.009    0.009    0.009 lesson_4.2.py:10(my_funk)
        1    0.000    0.000    0.009    0.009 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

с решетом        
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 lesson_4.2.py:24(sieve_erot)
        1    0.000    0.000    0.000    0.000 lesson_4.2.py:26(<listcomp>)
        1    0.000    0.000    0.000    0.000 lesson_4.2.py:34(<listcomp>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method math.ceil}
        1    0.000    0.000    0.000    0.000 {built-in method math.log}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''

'''
Итог:
    - время работы в решете при удвоении i возрастает в 2,5 или 3 раза, без него в 5
    - кол-во операций при решете 8 без решета 4
'''


















