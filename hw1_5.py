#5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = int(input('Введите значение выручки в рублях: '))
costs = int(input('Введите значение издержек в рублях: '))

if proceeds > costs:
    clean_profit = proceeds - costs
    profitability = clean_profit/proceeds
    print('Поздравляю! Отличная работа, чистая прибыль предприятия состовляет - ', clean_profit, 'рентабельность - ', profitability)
    workers = int(input('Введите колличество работников в фирме: '))
    profit_work = clean_profit/workers
    print('Чистая прибыль на одного сотрудника состовляет - ', profit_work)
elif proceeds == costs:
    print('К сожалению чистая прибыль у фирмы отсутствует')
else:
    print('Чистая прибыль отсутствует, также у фирмы расходы превышают доходы')