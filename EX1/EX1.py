# Напишите программу, которая принимает на вход 
# вещественное число и показывает сумму его цифр.

number = float(input("Введите число: "))
sum = 0

for i in str(number):
    if i != ".":
        sum += int(i)
print(sum)