import itertools

money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

from itertools import count

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
month = 0
while True:
    month += 1
    debt = spend - salary #Задолженность под конец месяца
    money_capital += salary - spend #Денежный капитал под конец месяца
    spend += spend * increase #Отражает увеличение трат с каждым следующим месяцом
    if money_capital < debt: #Условие завершения цикла - задолженносить привысит денежные накопленя
        break
print("Количество месяцев, которое можно протянуть без долгов:", month)
