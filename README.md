# Dog API

Dog API — это проект на Django с использованием Django REST Framework, предназначенный для управления данными о собаках и породах. Проект включает административный интерфейс Django, набор REST API для работы с моделями Dog и Breed, а также настроенную контейнеризацию через Docker и Docker Compose.

## Архитектура проекта

Проект состоит из следующих основных компонентов:

- **Приложение Dogs**  
  Содержит модели:
  - **Dog** — модель для представления данных о собаках (имя, возраст, пол, цвет, любимая еда, любимая игрушка, связь с породой).
  - **Breed** — модель для представления данных о породах (название, размер, дружелюбие, обучаемость, линька, потребности в упражнениях).

- **API**  
  Реализовано через Django REST Framework с использованием ViewSet-ов:
  - **DogViewSet** — предоставляет CRUD-операции для модели Dog, с дополнительными вычисляемыми полями (средний возраст собак породы, количество собак той же породы).
  - **BreedViewSet** — предоставляет CRUD-операции для модели Breed с вычисляемым полем (количество собак породы).

- **Административный интерфейс Django**  
  Позволяет управлять моделями Dog и Breed через стандартную панель администратора.

- **Контейнеризация с Docker**  
  Проект включает Dockerfile для сборки образа приложения и файл docker-compose.yml для одновременного запуска контейнеров приложения и базы данных (PostgreSQL).

- **Настройка окружения**  
  Переменные окружения задаются через файл `.env` (шаблон — `.env.template`), который содержит настройки подключения к базе данных и секретный ключ Django.

## Установка и запуск

### Требования

- [Docker](https://www.docker.com/) и [Docker Compose](https://docs.docker.com/compose/)  
- Git

### Шаги установки

1. **Клонирование репозитория**

   ```bash
   git clone https://github.com/AleksGin/Django_practice.git
   cd <dog_site>
   
2. Создание и настройка файла .env
   
  ```bash
  Скопируйте шаблон .env.template в файл .env и заполните его необходимыми значениями:
  ```
Отредактируйте файл .env, указав реальные значения для переменных окружения:

```plaintext
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_password
DB_HOST=your_host
DB_PORT_EXTERNAL=external_db_port
DB_PORT=your_port
SECRET_KEY=secret_key
```
3. Сборка и запуск контейнеров

Запустите сборку и запуск контейнеров с помощью Docker Compose:

```bash
docker-compose up --build
```
После завершения сборки и запуска контейнеров, приложение будет доступно по адресу http://localhost:8000.

4. Применение миграций

При первом запуске необходимо применить миграции для создания структуры базы данных:

```bash
docker-compose exec web-app python manage.py migrate
```

5. Создание суперпользователя (опционально)

Для доступа к административному интерфейсу Django создайте суперпользователя:

```bash
docker-compose exec web-app python manage.py createsuperuser
```

После этого вы сможете войти в административную панель по адресу http://localhost:8000/admin.


# Использование API

## Доступные эндпоинты

### Собаки (Dogs)

- GET /dogs/ — список всех собак.

- POST /dogs/ — создание новой записи о собаке.

- GET /dogs/{id}/ — получение информации о конкретной собаке.

- PUT /dogs/{id}/ — обновление информации о собаке.

- PATCH /dogs/{id}/ — частичное обновление информации о собаке.

- DELETE /dogs/{id}/ — удаление записи о собаке.

### Породы (Breeds)

- GET /breeds/ — список всех пород.

- POST /breeds/ — создание новой записи о породе.

- GET /breeds/{id}/ — получение информации о конкретной породе.

- PUT /breeds/{id}/ — обновление информации о породе.

- PATCH /breeds/{id}/ — частичное обновление информации о породе.

- DELETE /breeds/{id}/ — удаление записи о породе.


## Примеры запросов

### Получение списка всех собак: 
- GET http://localhost:8000/dogs/

  ```python
  {
    "id": 1 # Уникальный идентификатор записи о собаке. 
    "name": "Бадди", # Имя собаки. Это поле содержит текстовое значение.
    "age": 10, # Возраст собаки в годах
    "breed": "Чихуа-хуа", # Название породы собаки. В данном случае это "Чихуа-хуа". Это поле связано с моделью Breed.
    "breed_avg_age": 7.5, # Средний возраст собак той же породы, округлённый до одного знака после запятой.
                          # Это поле вычисляется динамически на основе данных в базе.
    "same_breed_count": 2, # Количество собак той же породы в базе данных.
    "gender": "Муж", # Пол собаки.
    "color": "Коричнево-белый", # Цвет собаки.
    "favorite_food": "Корм", # Любимая еда собаки.
    "favorite_toy": "Мячик" # Любимая игрушки собаки.
  }
  ```

# Остановка и удаление контейнеров

### Для остановки и удаления контейнеров выполните:

```bash
docker-compose down
```

### Если вы хотите также удалить том с данными PostgreSQL, используйте:

```bash
docker-compose down -v
```


### Этот README предоставляет обзор проекта, инструкции по установке и использованию, а также примеры запросов к API.
