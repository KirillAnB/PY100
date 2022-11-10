money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
def how_to_survive(bag, life_cost, money, inflation):
    month = 0 #Счетчик месяцев
    while bag > 0:
        bag = bag - life_cost #Тратим деньги в месяц
        bag = bag + money # Получаем зарплату
        life_cost = life_cost + life_cost * inflation # Увеличиваем расходы с учетом инфляции
        month += 1 # Добавляем месяц
    return month

months_to_zero = how_to_survive(money_capital, spend, salary, increase)
print(months_to_zero)
