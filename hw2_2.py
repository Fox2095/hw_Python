# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

mydata = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(mydata)
if len(mydata) % 2 == 0:
    i = 0
    while i < len(mydata):
        element = mydata[i]
        mydata[i] = mydata[i+1]
        mydata[i+1] = element
        i += 2
else:
    i = 0
    while i < len(mydata) - 1:
        element = mydata[i]
        mydata[i] = mydata[i + 1]
        mydata[i + 1] = element
        i += 2
print(mydata)