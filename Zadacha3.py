# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


lst = [1.1, 1.2, 3.1, 5, 10.01]
lst1 = []

# первый вариант
# for i in range(len(lst)):
#     n = round(lst[i] % 1, 5)
#     lst1.append(n)
#     if n == 0:
#         lst1.remove(0)

# Второй вариант
# lst1 = [round(n % 1, 5) for n in lst]  # list comprehension
# for i in range(len(lst1) - 1):    
#     if lst1[i] == 0: lst1.remove(0)

# Финальный вариант
lst1 = [round(n % 1, 5) for n in lst] 
lst1 = (list(filter(lambda x: x % 1 > 0, lst1)))

print(lst1)


def ost(lst_):
    min = float('inf')
    max = float('-inf')
    for i in range(len(lst_)):
        m = lst_[i]
        if min > m:
            min = m
        if max < m:
            max = m
        fin = max - min
    return fin


print(ost(lst1))