#2. Пользователь вводит время в секундах. Переведите время в часы,
# минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds_n = int(input('Введите время в секундах: '))
minute = 60 # в одной минуте 60 секунд
hours = 60 * 60 # в одном часе 3600 секунд
day = 60 * 60 * 24 # в одном дне 86 400 секунд

day1 = seconds_n // day
hour = (seconds_n - (day1)) // hours
minut = (seconds_n - (day1 + (hour * hours))) // minute
seconds = seconds_n - (day1 + (hour * hours) + (minut * minute))

print('{}:{}:{}'.format(hour, minut, seconds))