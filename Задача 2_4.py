# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
#  Позиции вводит пользователь через пробел.
# Реализуйте алгоритм перемешивания списка.

N = int(input("Введите число, для заполнения списка: "))

spisok = [N for N in range(-N, N+1)]

print(spisok)

multiply = spisok[int(input("Введите позицию первого числа: "))] * \
    spisok[int(input("Введите позицию второго числа: "))]

print("Произведение двух чисел =",multiply)

