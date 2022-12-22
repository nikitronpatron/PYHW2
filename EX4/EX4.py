# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях.

import random

number = int(input("Введите число: "))

for i in range (1, number + 1):
    i = random.randint(-number, number)
    print(i)