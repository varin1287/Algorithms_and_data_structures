'''
Посчитать четные и нечетные цифры введенного натурального числа. Например, если
введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
'''
def my_funk(even, odd, n ):
    if n == 0:
        return f'в числе {even} четных и {odd} нечетных цифр'
    else:
        if (n % 10) % 2 == 0:
            even += 1
        else:
            odd += 1
    return my_funk(even, odd, n // 10)


n = int(input('введите натуральное число: '))
even = 0
odd = 0

print(my_funk(even, odd, n ))










