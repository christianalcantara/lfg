from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter

from apps.proposal.api.views import LoanApplicationViewSet, ProposalViewSet, ValueViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("proposal/proposal", ProposalViewSet)
router.register("proposal/loan_application", LoanApplicationViewSet)
router.register("proposal/value", ValueViewSet)


app_name = "api"
urlpatterns = router.urls
