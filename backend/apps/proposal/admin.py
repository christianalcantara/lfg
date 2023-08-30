from django.contrib import admin

from .models import Field, LoanApplication, Proposal, Value


class FieldAdminInLine(admin.TabularInline):
    model = Field
    extra = 1


class ValueAdminInLine(admin.TabularInline):
    model = Value
    readonly_fields = (
        "field",
        "value",
    )
    can_delete = False
    max_num = 0


@admin.register(Proposal)
class ProposalAdmin(admin.ModelAdmin):
    verbose_name_plural = "1. Toppings"
    inlines = (FieldAdminInLine,)
    list_display = ("name",)


@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    inlines = (ValueAdminInLine,)
    list_display = (
        "id",
        "proposal",
        "creation_date",
        "approved",
    )
    list_display_links = (
        "id",
        "proposal",
    )
    list_filter = ("proposal", "approved")
    readonly_fields = (
        "proposal",
        "approved",
    )


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ("label", "name", "field_type", "proposal")
    list_filter = ("proposal", "field_type")


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    list_display = ("loan_application", "field", "value")
    list_filter = ("loan_application",)
