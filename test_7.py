import csv
import random

def generate_csv(N, header):
    pass

# Генерация значений в зависимости от типа колонки
if col_type == "int":
    for _ in range(N):
        value = random.randint(0, 100)
        column.append(str(value))
elif col_type == "str":
    for _ in range(N):
        length = random.randint(1, 100)
        text = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))
        column.append(text)
elif col_type == "bool":
    for _ in range(N):
        value = random.choice([True, False])
        column.append(str(value))


