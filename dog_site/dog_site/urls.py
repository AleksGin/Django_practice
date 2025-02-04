"""Конфигурация URL для проекта.

Настраивает маршруты для административной панели Django и API, реализованного через Django REST Framework.
Используется SimpleRouter для автоматической генерации маршрутов для ViewSet-ов.

Доступные URL:
  - /admin/ — административная панель Django.
  - /api/dogs/ — CRUD-операции для модели Dog через DogViewSet.
  - /api/breeds/ — CRUD-операции для модели Breed через BreedViewSet.

Пример использования:
  Если сервер запущен на localhost и порт 8000, то:
    - Админка доступна по http://localhost:8000/admin/
    - API для собак доступно по http://localhost:8000/api/dogs/
    - API для пород доступно по http://localhost:8000/api/breeds/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from dogs.views import (DogViewSet, BreedViewSet)

router = SimpleRouter()

router.register(prefix=r"dogs", viewset=DogViewSet)
router.register(prefix=r"breeds", viewset=BreedViewSet)

urlpatterns = [
    path(route="admin/", view=admin.site.urls),
    path(route="api/", view=include(router.urls)),
]

