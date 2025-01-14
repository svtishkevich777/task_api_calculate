# FastAPI Task Сalculate.


### Описание проекта находится в корне проекта, файл task.md.

## Установка и настройка.

### Системные требования.

- Python 3.8 и выше.

### Шаги для установки

1. Клонируйте репозиторий:

   ```sh
   $ git clone git@github.com:svtishkevich777/task_api_calculate.git
   $ cd task_api_calculate
   ```
2. Установите сторонний пакет virtualenv.
   
   ```sh
   $ pip install virtualenv
   ```
3. Создайте и активируйте виртуальное окружение:
   
   ```sh
   $ virtualenv -p python3 .venv -> укажите свою версию pythonX.X
   $ source .venv/bin/activate
   ```
4. Установите необходимые зависимости:
   ```sh
   (.venv)$ pip install -r requirements.txt
   ```

5. Запуск приложения.

   Для запуска FastAPI сервера выполните команду:
   ```sh
   $ uvicorn main:app --reload
   ```
6. Настройте переменные окружения.

   В корне проекта создайте файл .env и добавьте следующие переменные:
   ```
   URL_HOST=<ваш хост>
   URL_PORT=<ваш порт>
   ```
7. Настройка Docker.

   Для запуска приложения с помощью Docker выполните команду:

      ```sh
      $ docker-compose up --build
      ```
8. Доступные конечные точки:
   ```
   get method -> http://0.0.0.0:8000/calculate
   ```
   Для отправки данных, используйте следующий формат:

   ```
   http://0.0.0.0:8000/calculate?x=<значение>&y=<значение>
   ```
   Где <значение> — это целое число, которое вы хотите передать в параметры x и y.

   Пример запроса:
   ```
   http://0.0.0.0:8000/calculate?x=2&y=4   
   ```
   ### Принцип работы кода
   В директории tasks есть файл scripts_for_tasks,
   
   который нужно запустить для работы пользовательского интерфейса.
      
   ```
   print("Выберите задачу для выполнения:")
   print("1 - Выполнить task_1 (печать результатов запросов по порядку.)")
   print("2 - Выполнить task_2 (печать второго выполненного запроса и отмена остальных.)")
   print("3 - Выполнить task_3 (обработка третьего завершившегося запроса.)")
   print("0 - Выйти.")
   ```
   Пользовательский интерфейс позволяет выбирать, какую задачу выполнить.

   Приложение обрабатывает асинхронные запросы и возвращает результаты по выбранной задаче.
