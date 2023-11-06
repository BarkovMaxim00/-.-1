# TODO Напишите функцию для поиска индекса товара
def find_index(list_, value):   #Входные значения: "list_" - список товаров и "value" - список товаров, которые нужно найти.
    for fruit in list_:
        if fruit == value:      #Условие присуствует ли в списке "list_" товар, который нужно найти "value".
            return list_.index(value)
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
