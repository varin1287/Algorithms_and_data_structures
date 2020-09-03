'''
Определение количества различных подстрок с использованием хеш-функции.
'''

def num_str(my_str):
    hash_set = set()
    for i in range(len(my_str)):
        for j in range(i + 1, len(my_str) + 1):
            # в hash_set не вносим всю строку
            # другой вариант: вместо условия в строке 14 ставим len(hash_set) - 1
            if len(my_str[i:j]) == len(my_str):
                continue
            hash_set.add(hash(my_str[i:j]))
    return len(hash_set)

my_str = (input("введите строку : "))

print('количество различных подстрок: ', num_str(my_str))









