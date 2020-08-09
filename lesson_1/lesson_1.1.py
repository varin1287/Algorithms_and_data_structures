'''
Найти сумму и произведение цифр трехзначного числа,
которое вводит пользователь.
'''
x = int(input('введите целое, трёхзначное число: '))

rez_sum = x % 10
rez_mult = x % 10

x = x // 10
rez_sum = rez_sum + x % 10
rez_mult = rez_mult * (x % 10)

x = x // 10
rez_sum = rez_sum + x
rez_mult = rez_mult * x

print(f'сумма цифр равна {rez_sum}, а их произведение {rez_mult}')











