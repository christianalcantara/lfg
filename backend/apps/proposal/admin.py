from django.contrib import admin, messages
from django.http import HttpResponseRedirect

from .choices import LoanStatus
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
    inlines = (FieldAdminInLine,)
    list_display = ("name",)


@admin.register(LoanApplication)
class LoanApplicationAdmin(admin.ModelAdmin):
    change_form_template = "admin/proposal/change_form.html"

    inlines = (ValueAdminInLine,)
    list_display = (
        "partner_name",
        "partner_document",
        "proposal",
        "creation_date",
        "status",
    )
    list_filter = ("proposal", "status")
    search_fields = ("partner_name", "partner_document")
    readonly_fields = (
        "partner_name",
        "partner_document",
        "proposal",
        "status",
    )

    def has_add_permission(self, request, obj=None):
        return False

    def response_change(self, request, obj):
        if "_approve" in request.POST:
            obj.status = LoanStatus.APPROVED
            obj.save()
            self.message_user(request, f"{obj} Approved!")
            return HttpResponseRedirect(".")
        if "_negate" in request.POST:
            obj.status = LoanStatus.NOT_APPROVED
            obj.save()
            self.message_user(request, f"{obj} Not Approved!", level=messages.WARNING)
            return HttpResponseRedirect(".")
        return super().response_change(request, obj)


# @admin.register(Field)
# class FieldAdmin(admin.ModelAdmin):
#     list_display = ("label", "name", "field_type", "proposal")
#     list_filter = ("proposal", "field_type")
#
#
# @admin.register(Value)
# class ValueAdmin(admin.ModelAdmin):
#     list_display = ("loan_application", "field", "value")
#     list_filter = ("loan_application",)
#
#     def has_add_permission(self, request, obj=None):
#         return False
