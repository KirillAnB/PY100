from random import randint
def get_unique_list_numbers() -> list[int]:
    list_ = []
    # list_= [randint(-10,10) for _ in range(15) if _ not in list_]
    while len(list_)<15:
        num = randint(-10,10)
        if num not in list_:
            list_.append(num)
    return list_



list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
