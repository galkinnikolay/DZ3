# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве
# A[1..N]. Пользователь в первой строке вводит натуральное число N – количество 
# элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

# N = int(input('Введите кол-во элементов: '))
# X = int(input('Введите число для поиска: '))
# list = [i+1 for i in range(N)]
# count = 0
# print(list)
# if X in list:
#     count += 1
# print(count)


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к 
# заданному числу X. Пользователь в первой строке вводит натуральное число N – 
# количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

# N = int(input('Введите кол-во элементов: '))
# X = int(input('Введите число для поиска: '))
# list = [i for i in range(N)]
# count = list[0]
# print(list)
# for i in range(1, len(list)):
#     if X - list[i] < X - count:
#         count = list[i]
#     if X - list[i] == 0:
#         break
# print (count)