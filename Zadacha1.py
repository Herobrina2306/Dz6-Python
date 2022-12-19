# 1 предложить улучшения кода для четырёх уже решённых задач:

# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension


# Начиная с 3 семинара.

# Напишите программу, удаляющую из файла все слова, содержащие "абв".

with open ('text.txt', 'r', encoding = 'utf-8') as f:
    lst = list(map(str, f.readline().split()))

print(lst)


substring = 'абв'
output_txt = filter(lambda x: x.lower().find(substring) == -1, lst) # фильтр и лямбда
print(*output_txt)