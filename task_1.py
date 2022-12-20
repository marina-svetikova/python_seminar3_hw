# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной 
# позиции.

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random 
arr = []
for i in range(5): 
     arr.append(random.randint(0, 10))
print(f'случайный список {arr}')
sum=0
for i in range(len(arr)):
    if i%2!=0:
        sum = sum + arr[i]
print (sum)
