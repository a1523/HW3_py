# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на 
# нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list = input('Введите список чисел через пробел: ').split()
sum = 0
for i in range(1, len(list), 2):
    sum += int(list[i])
print('Сумма чисел на нечетных позициях', sum)