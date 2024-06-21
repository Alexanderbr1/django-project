# Используем официальный образ Python
FROM python:3.12.2

# Устанавливаем переменную окружения для вывода логов в консоль
ENV PYTHONUNBUFFERED 1

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файлы зависимостей (requirements.txt) в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости проекта
RUN pip install -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /app/

# Опционально: собираем статические файлы (если они используются)
# RUN python manage.py collectstatic --noinput

# Опционально: выполняем миграции базы данных
RUN python manage.py migrate

# Опционально: запускаем команды, необходимые для подготовки проекта
# RUN python manage.py <your_custom_command>

# Определяем порт, который будет доступен извне контейнера
EXPOSE 8000

# Команда для запуска сервера Django при старте контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
