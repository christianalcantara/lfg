from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "apps.core.fields.UUIDAutoField"
    name = "apps.core"
