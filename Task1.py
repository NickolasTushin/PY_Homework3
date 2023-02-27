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
