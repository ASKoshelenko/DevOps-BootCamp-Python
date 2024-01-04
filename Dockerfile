# Используйте официальный образ Python как базовый
FROM python:3.8-slim

# Установите рабочий каталог в контейнере
WORKDIR /app

# Копируйте файлы зависимостей и установите их
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копируйте остальные файлы проекта
COPY . .

# Запуск приложения
CMD ["python", "start.py"]
