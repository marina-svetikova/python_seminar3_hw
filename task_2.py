# 2'. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем 
# первый и последний элемент, второй и предпоследний и т.д.

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import random 
arr = []
for i in range(5): 
     arr.append(random.randint(0, 10))
print(f'случайный список {arr}')
new_arr = []
for i in range(int(len(arr)+1)//2):
     new_arr.append(arr[i]*arr[(len(arr)-i)-1])
print(f'новый список {new_arr}')
