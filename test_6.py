import csv
import argparse

def validate_csv_file(file_path, header=True, delimiter=','):
    # Чтение CSV файла
    with open(file_path, 'r') as file:
        csv_data = csv.reader(file, delimiter=delimiter)

        # Проверка наличия заголовка
        if header:
            file_header = next(csv_data)

        # Валидация данных
        for row in csv_data:
            # Проверка, что количество элементов в строке соответствует количеству заголовков (если присутствует)
            if header and len(row) != len(file_header):
                return False, 'Количество элементов в строке не соответствует количеству заголовков'

    return True, 'Файл прошел валидацию'

