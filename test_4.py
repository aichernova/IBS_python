import tempfile

class TempFileManager:
    def __enter__(self):
        # Создаем временный файл в бинарном режиме (mode='wb')
        self.temp_file = tempfile.TemporaryFile(mode='w+b')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Выполняется при окончании работы с контекстом

        # Переходим в начало файла
        self.temp_file.seek(0)

        # Читаем содержимое файла и выводим
        content = self.temp_file.read()
        print(f"Содержимое файла: {content.decode()}")

        # Переходим в начало файла
        self.temp_file.seek(0)

        # Печатаем количество символов в файле
        print(f"Количество символов в файле: {len(content)}")

        # Закрываем временный файл
        self.temp_file.close()

    def repeat(self):
        # Переходим в начало файла
        self.temp_file.seek(0)

        # Читаем содержимое файла
        content = self.temp_file.read()

        # Переходим в конец файла
        self.temp_file.seek(0, 2)

        # Дублируем содержимое файла и добавляем в конец
        self.temp_file.write(content)

    def write(self, msg):
        # Переходим в начало файла
        self.temp_file.seek(0)

        # Читаем содержимое файла
        content = self.temp_file.read()

        # Переходим в начало файла
        self.temp_file.seek(0)

        # Записываем текст в начало файла
        self.temp_file.write(msg.encode() + content)

    def show(self):
        # Переходим в начало файла
        self.temp_file.seek(0)

        # Читаем и выводим содержимое файла
        content = self.temp_file.read()
        print(content.decode())

# Использование контекстного менеджера
with TempFileManager() as manager:
    # Дублируем текущее содержание файла и добавляем в конец файла
    manager.repeat()

    # Записываем текст в начало файла
    manager.write("Привет, мир!")

    # Выводим содержимое файла
    manager.show()
