# Задайте список из n чисел последовательности 
# $(1+\frac 1 n)^n$ и выведите на экран их сумму.

number = int(input("Введите число: "))
sum = 0

for i in range (1, number + 1):
    equation = round((1 + 1 / i)**i, 0)
    sum += equation
    print(f"{i}: {sum}, ")