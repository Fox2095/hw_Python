# 6. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.

list_product = []
while input("Хотите добавить товар? Введите да / нет: ") == 'да':
    number = int(input("Введите номер продукта:"))
    product = {}
    while input("Хотите добавить параметры продукта? Введите да / нет: ") == 'да':
        product_key = input("Введите наименование характеристики товара: ")
        product_value = input("Введите значение характеристики товара: ")
        product[product_key] = product_value
    list_product.append(tuple([number, product]))
print(list_product)

analysis = {}
for l_product in list_product:
    for product_key, product_value in l_product[1].items():
        if product_key in analysis:
            analysis[product_key].append(product_value)
        else:
         analysis[product_key] = [product_value]
print(analysis)
