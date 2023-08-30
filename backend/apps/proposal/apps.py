from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ProposalConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.proposal"
    verbose_name = _("Management of Loan Proposals")
