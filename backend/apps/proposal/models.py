from django.db import models
from django.utils.translation import gettext_lazy as _

from .choices import FieldTypes


class Proposal(models.Model):
    name = models.CharField(verbose_name=_("Proposal Name"), max_length=100)

    class Meta:
        verbose_name = _("Proposal")
        verbose_name_plural = _("Proposals")

    def __str__(self):
        return self.name


class LoanApplication(models.Model):
    creation_date = models.DateTimeField(
        verbose_name=_("Creation Date"), editable=False, blank=True, auto_now_add=True
    )
    proposal = models.ForeignKey(
        verbose_name=_("Proposal"),
        to=Proposal,
        on_delete=models.PROTECT,
        related_name="loan_applicattions",
    )
    approved = models.BooleanField(verbose_name=_("Approved"), default=None, null=True)

    class Meta:
        verbose_name = _("Loan Application")
        verbose_name_plural = _("Loan Requests")

    def __str__(self):
        return f"[{self.id}] {self.proposal}"


class Field(models.Model):
    proposal = models.ForeignKey(
        verbose_name=_("Proposal"),
        to=Proposal,
        on_delete=models.CASCADE,
        related_name="fields",
    )
    name = models.CharField(verbose_name=_("Name"), max_length=50, help_text=_("Field name."))
    label = models.CharField(
        verbose_name=_("Label"),
        max_length=100,
        help_text=_("Text to be displayed in the field."),
    )
    field_type = models.CharField(verbose_name=_("Field Type"), max_length=7, choices=FieldTypes.choices)
    required = models.BooleanField(verbose_name=_("Required"), default=True, help_text=_("Field is required?"))

    class Meta:
        verbose_name = _("Proposal Field")
        verbose_name_plural = _("Proposal Fields")
        unique_together = ("proposal", "name")

    def __str__(self):
        return f"{self.label}"


class Value(models.Model):
    loan_application = models.ForeignKey(
        verbose_name=_("Loan Application"),
        to=LoanApplication,
        on_delete=models.CASCADE,
        related_name="values_loan_applicattions",
    )
    field = models.ForeignKey(
        verbose_name=_("Field"),
        to=Field,
        on_delete=models.PROTECT,
        related_name="values_field",
    )
    value = models.CharField(verbose_name=_("Value"), max_length=255)

    class Meta:
        verbose_name = _("Field Value")
        verbose_name_plural = _("Fields Value")
        unique_together = ("field", "loan_application")

    def __str__(self):
        return f"{self.field.label}: {self.value}"
