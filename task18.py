# Задача 18: Требуется найти в массиве A[0..N-1] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6

# -> 5

n = int(input('Input number of elements in the list: '))
list_A = [0] * n

for i in range(len(list_A)):
    list_A[i] = int(input(f'Enter the value of {i}th element: '))
print (list_A)

X = int(input('Set the value of the number: '))
near_element = 0

for i in range(1, len(list_A)):
    if abs(X - list_A[i]) < abs(X - list_A[i-1]):
        near_element = list_A[i]
print(near_element)