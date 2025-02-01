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
    queryset = Breed.objects.annotate(
        dogs_breed_count=Count(
            "dogs",
            distinct=True,
        )
    )
    serializer_class = BreedSerializer
