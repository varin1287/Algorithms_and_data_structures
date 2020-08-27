'''
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
'''

# Использован урок 2 задание 3
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.

# !!! Есть вопрос написсан после отчета

import random
import sys

sys.setrecursionlimit(10000)

def show(x):
    #print(f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')
    global res
    if type(x) != list:
        res += sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show(key)
                show(value)
        elif not isinstance(x, str):
            for item in x:
                show(item)


def my_func_1(n, result=0):
    if n == 0:
        my_list.extend([result, n])
        return f'вар 1: {result}'
    else:
        return my_func_1(n // 10, result * 10 + n % 10)

def my_func_2(n):
    result = 0
    while n > 0:
        result = result * 10 + n % 10
        n = n // 10
    my_list.extend([result, n])
    return f'вар 2: {result}'


def my_func_3(n):
    result = ''
    n = str(n)
    for i in n:
        result = i + result
    my_list.extend([result, n, i])
    return f'вар 3: {result}'


def my_func_4(n):
    n = str(n)
    result = n[::-1]
    my_list.extend([result, n])
    return f'вар 4: {result}'

def my_num(size):
    return random.randint(10 ** (size - 1), 10 ** size - 1)

SIZE = 100

n = my_num(SIZE)
print('исх. число - ', n)

all_funk = [my_func_1, my_func_2, my_func_3, my_func_4]
# Не знаю можно ли так, но вроде работает одинаково с отдельным вызовом каждой функции

for spam in all_funk:
    res = 0
    my_list = []
    print(spam(n))
    show(my_list)
    print(f'использовано памяти: {res}')

''' ОТЧЕТ
Система win 10, 64-bit
Python 3.8 32-bit 
n =                  10    100    1000    10000
вар 1: 
использовано памяти: 30    70     468     превышение стека тестировать не стал
вар 2: 
использовано памяти: 30    70     468     4454
вар 3: 
использовано памяти: 96    276    2076    20076
вар 4: 
использовано памяти: 70    250    2050    20050
Вывод: 
 -рекурсия и цикл по затратам памяти одинаковы и меньше чем в 3 и 4 вариантах
 -решения через строки и result = n[::-1] почти одинаковы, тратят памяти в 3.2, 3.9, 4.4, 4.5 раза больше,
    чем первые варианты. С увеличением кол-ва цифр в числе растет коэфициент.
 - по скорости 4 вар в два раза лучше 3 вар и в 40 раз лучше 2 и 1 вар (примерно)
ИТОГ: В зависимости от того нужна скорость или экономим память выбираем нужный вариант. 
   

'''


def show_test(x):
    print(f'type={type(x)}, size={sys.getsizeof(x)}, obj={x}')

# два способа добавления в my_list занимают разный объем памяти, хотя оба list равны. Почему так?
# разница в 4 байта
def my_func_1(n, result=0):
    if n == 0:
        my_list.extend([result, n])
        my_list_1.append(result)
        my_list_1.append(n)
        return f'вар 1: {result}'
    else:
        return my_func_1(n // 10, result * 10 + n % 10)

my_list = []
my_list_1 = []

n = my_num(5)
print(my_func_1(n))
print(id(my_list), id(my_list_1))  #19557800 19557768
print(my_list == my_list_1) # True
show_test(my_list)   # type=<class 'list'>, size=48, obj=[23616, 0]
show_test(my_list_1) # type=<class 'list'>, size=44, obj=[23616, 0]




















