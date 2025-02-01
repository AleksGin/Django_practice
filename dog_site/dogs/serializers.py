from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import (
    Breed,
    Dog,
)


class DogSerializer(ModelSerializer):
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
    dogs_breed_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Breed
        fields = "__all__"
