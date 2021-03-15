# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def sumnum():
    try:
        with open('testfile5_5.txt', 'w+') as f_obj:
            type_text = input('Введите цифры через пробел: \n')
            f_obj.writelines(type_text)
            my_num = type_text.split()

            print(sum(map(int, my_num)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
sumnum()