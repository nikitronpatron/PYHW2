# Напишите программу, которая принимает на вход 
# число N и выдает набор произведений чисел от 1 до N.

number = range(int(input("Введите число: ")))
factorial = 1

for i in number:
    factorial *= (i + 1)
    print(factorial)