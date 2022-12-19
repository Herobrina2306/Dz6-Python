# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input(f'Введите число для массива: '))

lst = []

# for i in range(n + 1):
#     lst.append(i)
# print(*lst)   

lst = [i for i in range(n+1)]
print(*lst)

for m in range(2, len(lst)):
    lst[m] = lst[m - 1] + lst[m - 2]
print(*lst)

lst1 = []
lst_fin = []

for s in range(1, len(lst)):
    if s % 2 == 0:
        t = -lst[s]
        lst1.append(t)
    else:
        lst1.append(lst[s])
print(*lst1)


lst_fin = list(reversed(lst1)) + lst

print(lst_fin)