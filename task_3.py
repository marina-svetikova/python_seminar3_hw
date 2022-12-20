# 3'. Задайте список из вещественных чисел. Напишите программу,
#  которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19 (максимальное значение у числа 1.2 , минимальное у 10.01)
import random 
list = []
for i in range(5): 
      list.append(round(random.uniform(0, 10), 2))  # генератор случаных вещественных чисел
print (f'список: {list}')

# list = list(map(float, input('Введите:').split()))
# print(list)
# list = [1.1, 1.2, 3.1, 5, 10.01]
# print(f'Лист: {list}')

list_1 = []
for i in range(0,len(list)):
      list_1.append((list[i]*10)%10)
print(f'Лист: {list_1}')
max = (max(list_1))
min = (min(list_1))
print(f'max и min:{max} и {min}')
diff = (max-min)
print (f'Разница между мах и мин:{diff}')
