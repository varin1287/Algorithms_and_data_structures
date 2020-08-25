'''
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
'''


from collections import namedtuple
from collections import deque

Company = namedtuple('Company', 'name, profit_1, profit_2, profit_3, profit_4, sum_profit')


namber = int(input('введите кол-во предприятий: '))
my_list = deque()   # смысла в deque я бы поставил list
sr_profit = 0
for i in range(namber):
    my_list.append(Company(input('введите имя: '), int(input('введите прибыль за 1-ый квартал: ')), int(input('введите прибыль за 2-ый квартал: ')),
                           int(input('введите прибыль за 3-ый квартал: ')), int(input('введите прибыль за 4-ый квартал: ')), None ))

    my_list[i] = my_list[i]._replace(sum_profit=(my_list[i].profit_1 + my_list[i].profit_2 + my_list[i].profit_3 + my_list[i].profit_4))
    sr_profit = (sr_profit + my_list[i].sum_profit)
sr_profit /= (i + 1)

print('средняя прибыль ', sr_profit)

for i in my_list:
    if i.sum_profit > sr_profit:
        print(f'компания {i.name} получила прибыль выше средней на {i.sum_profit - sr_profit}')
    elif i.sum_profit < sr_profit:
        print(f'компания {i.name} получила прибыль ниже средней на {i.sum_profit - sr_profit}')
    else:
        print(f'компания {i.name} получила среднюю прибыль ')















