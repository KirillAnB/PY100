money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
def how_to_survive(bag, life_cost, money, inflation):
    month = 0
    while bag > 0:
        bag = bag + money
        bag = bag - life_cost
        life_cost = life_cost + life_cost * inflation
        month += 1
    return month

answer = how_to_survive(money_capital, spend, salary, increase)
print(answer)
