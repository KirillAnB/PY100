# def delete(list_, index=None):
#     if index is None:
#         index = len(list_) - 1
#         list_.pop(index)
#     else:
#         list_.pop(index)
#     return list_
def delete(list_, index=None):
    if index is None:
         list_ = list_[:-1]
         return list_
    elif index == 0:
        list_ = list_[index+1:]
        return list_
    else:
        list_1 = list_[:index]
        list_2 = list_[index +1:]
        list_ = list_1 + list_2
        return list_



print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]

