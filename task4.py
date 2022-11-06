from random import choice


EAGLE = "Орел"
TAILS = "Решка"

coin = [EAGLE, TAILS]  # монета, для которой нужно выбрать случайную сторону
counts = [10, 100, 1000, 100000, 1000000]  # различное количество подбрасываний
list_freq = []  # список, где будем хранить отношение количества выпавших орлов к решке

for count in counts:
    x,y = 0,0
    for i in range(count):
        side = choice(coin)
        if side == coin[0]:
            x +=1
        else:
            y +=1
    if x < y:
        list_freq.append(x / y)
    else:
        list_freq.append((y / x))
print(list_freq)

    # TODO разделить минимальное число среди орлов и решек на максимальное число и сохранить результат

# print(list_freq)
