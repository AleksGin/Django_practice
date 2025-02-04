from django.contrib import admin

from .models import (
    Breed,
    Dog,
)


@admin.register(Dog)
class DogModelAdmin(admin.ModelAdmin):
    pass
    """Административный интерфейс для модели Dog.

    Позволяет управлять записями о собаках через Django Admin.
    """


@admin.register(Breed)
class BreedModelAdmin(admin.ModelAdmin):
    pass
    """Административный интерфейс для модели Breed.

    Позволяет управлять записями о породах через Django Admin.
    """
