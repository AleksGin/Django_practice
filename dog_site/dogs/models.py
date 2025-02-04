from django.core.validators import (
    MaxValueValidator,
    MinValueValidator,
)
from django.db import models


class Dog(models.Model):
    """Модель для представления собаки в базе данных.

    Attributes:
        name (CharField): Имя собаки.
        age (IntegerField): Возраст собаки.
        breed (ForeignKey): Связь с породой собаки.
        gender (CharField): Пол собаки.
        color (CharField): Цвет собаки.
        favorite_food (CharField): Любимая еда собаки.
        favorite_toy (CharField): Любимая игрушка собаки.
    """

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
        """Возвращает строковое представление объекта Dog.

        Returns:
            str: Имя собаки.
        """
        return self.name


class Breed(models.Model):
    """Модель для представления породы собак в базе данных.

    Attributes:
        name (CharField): Название породы.
        size (CharField): Размер породы (Tiny, Small, Medium, Large).
        friendliness (IntegerField): Уровень дружелюбия (1-5).
        trainability (IntegerField): Уровень обучаемости (1-5).
        shedding_amount (IntegerField): Уровень линьки (1-5).
        exercise_needs (IntegerField): Уровень потребности в упражнениях (1-5).
    """
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
        """Возвращает строковое представление объекта Breed.

        Returns:
            str: Название породы.
        """
        return self.name
