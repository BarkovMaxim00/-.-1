# TODO импортировать необходимые молули
import csv
import json
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter = ',',  quotechar = '\n')
        reader_list = [content for content in reader]

    # TODO считать содержимое csv файла
    with open(OUTPUT_FILENAME, 'w') as json_file:
            json.dump(reader_list, json_file, indent = 4)

    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
