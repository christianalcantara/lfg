from django.db.models.fields import AutoFieldMixin, UUIDField


class UUIDAutoField(AutoFieldMixin, UUIDField):
    """Custom UUID Auto Field"""

    def get_internal_type(self):
        return "UUIDAutoField"

    def rel_db_type(self, connection):
        return UUIDField().db_type(connection=connection)
