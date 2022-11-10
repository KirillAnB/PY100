list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
# TODO найти сумму, количество и среднее арифметическое уникальных чисел
new_list_ = list(set(list_))
print(new_list_)

new_list_len = len(new_list_)
new_list_sum = sum(new_list_)

print(new_list_len, new_list_sum)