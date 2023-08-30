from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class FieldTypes(TextChoices):
    TEXT = "text", _("Text")
    NUMBER = "number", _("Number")
    TEL = "tel", _("Phone Number")
    DATE = "date", _("Date")
    EMAIL = "email", _("E-mail")


class ProposalStatus(TextChoices):
    APPROVED = "approved", _("Approved")
    NOT_APPROVED = "not_approved", _("Not Approved")
    WAITING_FOR_APPROVAL = "waiting_for_approval", _("Waiting for Approval")
