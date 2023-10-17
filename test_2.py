import logging
import time

# Функция, которая реализует декоратор
def cache_result(num_calls=3):
    # Словарь, где будем хранить кеш
    cache = {}

    # Функция-декоратор для вызова других функций
    def decorator(func):

        # Функция-обертка, которая будет заменять вызываемую функцию
        def wrapper(*args, **kwargs):
            # Создаем ключ для кеша, основываясь на аргументах функции
            key = (func.__name__, args, frozenset(kwargs.items()))

            # Проверяем, есть ли результат в кеше
            if key in cache:
                logging.info(f"Getting result from cache for {func.__name__} function")
                return cache[key]

            # Если необходимо вызывать функцию раз в num_calls вызовов, то обновляем кеш
            if len(cache) >= num_calls:
                cache.clear()

            # Выполняем вызов функции
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            # Сохраняем результат в кеше
            cache[key] = result

            # Выводим время выполнения
            logging.info(f"Execution time for {func.__name__} function: {end_time - start_time} seconds")

            return result

        return wrapper

    return decorator

# Пример использования декоратора
@cache_result(num_calls=2)
def my_function(x, y):
    time.sleep(1)  # Имитация долгой работы функции
    return x + y

# Вызываем функцию несколько раз
print(my_function(1, 2))  # Выведет время выполнения и результат (3)
print(my_function(3, 4))  # Выведет время выполнения и результат (7)
print(my_function(1, 2))  # Выведет результат из кеша, без времени выполнения (3)
print(my_function(5, 6))  # Выведет время выполнения и результат (11)
