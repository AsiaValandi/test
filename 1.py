# Бабак А.А., КНИТ17-Б
""""№1. Введите с клавиатуры 5 целочисленных значений.Выведите их в одну строку через запятую. Получите для массива
среднее арифметическое. """

import numpy as np

x = 5
A = np.zeros(x, dtype=int)

for i in range(x):
    while True:
        try:
            A[i] = int(input('>>>'))
            break
        except ValueError:
            print('\nНекорректный ввод. Пожалуйста, повторите еще раз.')

print('\nВаш массив:')
for i in range(x):
    if i < (x-1):
        print(A[i], end=', ')
    else:
        print(A[i], end='.\n')
print('\nСреднее значение элементов массива: ', np.mean(A))

