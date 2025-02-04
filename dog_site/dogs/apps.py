from django.apps import AppConfig


class DogsConfig(AppConfig):
    """Конфигурация приложения Dogs.

    Attributes:
        default_auto_field (str): Тип поля для автоматического создания первичного ключа.
        name (str): Имя приложения.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "dogs"
