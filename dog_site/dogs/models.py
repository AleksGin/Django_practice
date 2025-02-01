from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)
from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.ForeignKey(
        "Breed",
        on_delete=models.PROTECT,
        related_name="dogs",
    )
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    favorite_food = models.CharField(max_length=255)
    favorite_toy = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Breed(models.Model):
    name = models.CharField(max_length=40)

    SIZE_CHOISES = [
        ("Tiny", "Tiny"),
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
    ]
    size = models.CharField(max_length=10, choices=SIZE_CHOISES, default="Medium")

    friendliness = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    trainability = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    shedding_amount = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    exercise_needs = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self) -> str:
        return self.name
