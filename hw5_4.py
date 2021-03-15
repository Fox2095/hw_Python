# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1, Two — 2, Three — 3, Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = {'One' : 1, 'Two' : 2, 'Three' : 3, 'Four' : 4}
new_f = []
with open('testfile5_4.txt', 'r') as f_obj:
    content = f_obj.read().split('\n')
    for i in f_obj:
        i = i.split(' ', 1)
        new_f.append(rus[i[0]] + '  ' + i[1])
    print(new_f)

with open('testfile5_4.txt', 'w') as ff_obj:
    ff_obj.writelines(new_f)