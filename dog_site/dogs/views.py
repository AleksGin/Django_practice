from django.db.models import Avg, Count, F, OuterRef, Q, Subquery
from django.db.models.functions import Coalesce, Round
from rest_framework.viewsets import ModelViewSet

from .models import (
    Breed,
    Dog,
)
from .serializers import (
    BreedSerializer,
    DogSerializer,
)


class DogViewSet(ModelViewSet):
    """ViewSet для работы с объектами модели Dog.

    Этот ViewSet предоставляет CRUD-интерфейс для модели Dog. В наборе выборки (queryset)
    добавляются два аннотированных поля:
      - breed_avg_age: округлённое до одного знака после запятой среднее значение возраста собак
        той же породы. Если данные отсутствуют, используется значение 0.0.
      - same_breed_count: количество собак, относящихся к той же породе, с учётом уникальности.

    Атрибуты:
        queryset (QuerySet): Набор объектов Dog, аннотированных дополнительными полями.
        serializer_class (Serializer): Класс сериализатора, используемый для представления объектов Dog.

    Исключения:
        Может возникать django.db.utils.OperationalError, если база данных недоступна или
        настройки подключения неверны.
    """

    queryset = Dog.objects.annotate(
        breed_avg_age=Round(
            Coalesce(
                Subquery(
                    Dog.objects.filter(breed=OuterRef("breed"))
                    .values("breed")
                    .annotate(avg_age=Avg("age"))
                    .values("avg_age")[:1]
                ),
                0.0,
            ),
            1,
        ),
        same_breed_count=Count(
            "breed__dogs",
            filter=Q(breed__dogs__breed=F("breed")),
            distinct=True,
        ),
    )
    serializer_class = DogSerializer


class BreedViewSet(ModelViewSet):
    """ViewSet для работы с объектами модели Breed.

    Этот ViewSet предоставляет CRUD-интерфейс для модели Breed. В наборе выборки (queryset)
    для каждого объекта породы добавляется аннотированное поле:
      - dogs_breed_count: количество собак, связанных с данной породой (без повторов).

    Атрибуты:
        queryset (QuerySet): Набор объектов Breed, аннотированных полем dogs_breed_count.
        serializer_class (Serializer): Класс сериализатора, используемый для представления объектов Breed.

    Исключения:
        Может возникать django.db.utils.OperationalError, если при обращении к базе данных
        произошла ошибка подключения или настройки миграций не прошли корректно.
    """
    queryset = Breed.objects.annotate(
        dogs_breed_count=Count(
            "dogs",
            distinct=True,
        )
    )
    serializer_class = BreedSerializer
