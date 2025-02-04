# Этот Dockerfile используется для создания образа приложения Django.
# Основан на образе python:3.12-alpine.
#
# Переменные окружения:
#   PYTHONDONTWRITEBYTECODE - отключает запись байткода (.pyc) для упрощения разработки.
#   PYTHONUNBUFFERED        - отключает буферизацию вывода, что полезно для логирования в Docker.
#
# Шаги сборки:
#   1. Обновление списка пакетов и установка необходимых системных зависимостей:
#         libpq, libpq-dev (для работы с PostgreSQL),
#         gcc и musl-dev (для компиляции Python-зависимостей).
#   2. Установка зависимостей Python из файла requirements.txt.
#   3. Копирование исходного кода проекта в рабочую директорию.
#   4. Запуск сервера Django на 0.0.0.0:8000.

FROM python:3.12-alpine


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add --no-cache \
    libpq \
    libpq-dev \
    gcc \
    musl-dev

WORKDIR /dogs

COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY dog_site/ .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]