from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import (
    Breed,
    Dog,
)


class DogSerializer(ModelSerializer):
    """Сериализатор для модели Dog.

    Добавляет вычисляемые поля:
    - breed_avg_age: средний возраст собак этой породы.
    - same_breed_count: количество собак той же породы.

    Attributes:
        breed_avg_age (FloatField): Средний возраст породы.
        same_breed_count (IntegerField): Количество собак породы.
        breed (SlugRelatedField): Связь с породой через имя (slug).
    """

    breed_avg_age = serializers.FloatField(read_only=True)
    same_breed_count = serializers.IntegerField(read_only=True)
    breed = serializers.SlugRelatedField(
        queryset=Breed.objects.all(),
        slug_field="name",
    )

    class Meta:
        model = Dog
        fields = [
            "id",
            "name",
            "age",
            "breed",
            "breed_avg_age",
            "same_breed_count",
            "gender",
            "color",
            "favorite_food",
            "favorite_toy",
        ]


class BreedSerializer(ModelSerializer):
    """Сериализатор для модели Breed.

    Добавляет вычисляемое поле:
    - dogs_breed_count: количество собак этой породы.

    Attributes:
        dogs_breed_count (IntegerField): Количество собак породы.
    """

    dogs_breed_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Breed
        fields = "__all__"
