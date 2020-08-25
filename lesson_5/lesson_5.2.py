'''
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как
коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их
как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''
from  collections import deque

def my_input():
  my_list = []
  while True:
    num = input('введите цифру или букву (для завершения нажмите enter без ввода значения): ')
    if num == '':
      break
    my_list.append(num)
  return my_list

list_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

print(f'введите два шестнадцатеричных числа по одной цифре \nв формате{list_numbers}')
print('ввод 1-го числа ')
first = my_input()
print('ввод 2-го числа ')
second = my_input()
print(first, second)

#first = ['A','2']
#second = ['C', '4', 'F']

if len(first) < len(second):
  first, second = second, first

res = deque()
# при использовании reverse() в строках 26, 27, 37 используется i влместо len(first) - i - 1
# и добавление цифр при разной длинне чисел будет через цикл
# чуть позже сравню скорости в обоих случаях
#first.reverse()
#second.reverse()

k = 0
for i in range(len(first)):
  one = list_numbers.index(first[len(first) - 1]) # начинаю с последнего элемента
  two = list_numbers.index(second[len(second) - 1])
  first.pop(len(first) - 1)
  second.pop(len(second) - 1)
  res.appendleft(list_numbers[(one + two + k) % 16])
  if (one + two) >= 15:
    k = 1
  else:
    k = 0
  if len(second) == 0:
    res.extendleft(first)
    break
print('результат сложения - ', res)








