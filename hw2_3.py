# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict

n_month = int(input("Введите номер месяца: "))
if n_month <= 12 and n_month >= 1:
    # список <class 'dict'>
 seasons = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}
 for key in seasons.keys():
     if n_month in seasons[key]:
         print(key)

        # список <class 'list'>
 season = ['Зима', 'Весна', 'Лето', 'Осень']
 if n_month == 1 or n_month == 2 or n_month == 12:
     print(season[0])
 elif n_month >= 3 and n_month <= 5:
    print(season[1])
 elif n_month >= 6 and n_month <= 8:
     print(season[2])
 elif n_month >= 9 and n_month <= 11:
     print(season[3])
