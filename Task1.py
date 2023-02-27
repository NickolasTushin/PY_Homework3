"""
Первая задача:
Задаем длину списка наполненного рандомными числами от 1 до 100.
Вводим искомое число X
Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
"""
import random
num = int(input('Введите число: '))
list = []
k = 0
closest_num = -1
for i in range(15):
     list.append(random.randint(1,101))
     min_d = max(list) - num

     if int(list[i]) == num:
         k += 1
for i in set(list):
     if abs(i - num) < min_d:
         min_d = abs(i - num)
         closest_num = i
print(f'{k} раз встречается в заданном списке число {num}')


print(f'максимально близкое число {closest_num}')

print(f'список {list}')

print(f'список без повторных чисел {set(list)}')
