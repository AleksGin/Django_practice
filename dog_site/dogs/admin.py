from django.contrib import admin

from .models import (
    Breed,
    Dog,
)


@admin.register(Dog)
class DogModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Breed)
class BreedModelAdmin(admin.ModelAdmin):
    pass
