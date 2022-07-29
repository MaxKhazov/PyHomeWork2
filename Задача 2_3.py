# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.

n = int(input("Введите число: "))

def function(n):
    summ = 0
    for n in range (1,n+1):
        sum = (1 + 1/n)**n
        summ += sum
        print (n , summ, end= " ") 
function(n)
