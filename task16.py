# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[0..N-1]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3
# -> 1

N = int(input('Enter natural number: '))
A = [0] * N
for i in range(len(A)):
    A[i] = int(input(f'Enter the value of {i}th element: '))
print (A)
X = int(input('Enter the element value to search: '))
count = 0
for element in A:
    if element == X:
        count += 1
print (count)
