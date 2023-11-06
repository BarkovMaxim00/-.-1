# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, splitter = ","): #Входные данные: строка 1, строка 2 и разделяющий их элемент(по умолчанию - ",").
    str1 = str1.split(splitter) #Разделяет строки на основании заданного разделителя.
    str2 = str2.split(splitter)
    str1 = set(str1) #Превращает строки в множества для возможности работы с методом "intersection".
    str2 = set(str2)
    overlap = str1.intersection(str2) #Используется метод "intersection" для нахождения одинаковыхх в двух множествах значений строк.
    return sorted(list(overlap))
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group,"|"))