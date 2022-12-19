lst = [2, 3, 4, 5, 6, 7, 8, 9, 1, 11]


# def sum(lst_):
#     b = 0
#     for i in range(1, len(lst_), 2):
#         b += lst_[i]    
#     return b


# print(lst, ' -> ', sum(lst))

n = 0
for i, x in enumerate(lst):
    if i % 2 == 1:
        n = x + n

print(lst, ' -> ', n) 