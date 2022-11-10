salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
# Похожая на 8 задачу, решение чере цикл for
def how_to_survive2(bag, life, time, cash, infl):
    for i in range(1, time+1):
        bag += life
        bag -= cash
        life = life + life * infl
    return bag

answer = how_to_survive2(need_money, spend, months, salary, increase)
print(round(answer))
