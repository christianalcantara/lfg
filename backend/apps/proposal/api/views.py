from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from ..models import LoanApplication, Proposal, Value
from ..tasks import proccess_loan_requests
from .serializers import LoanApplicationSerializer, ProposalSerializer, ValueSerializer


class ProposalViewSet(
    CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, ListModelMixin, DestroyModelMixin, GenericViewSet
):
    serializer_class = ProposalSerializer
    queryset = Proposal.objects.all()


class LoanApplicationViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = LoanApplicationSerializer
    queryset = LoanApplication.objects.all()

    @action(detail=False, methods=["post"])
    def request(self, request, pk=None):
        # Endpoint para criar os valores para os campos passados pelo frontend
        data = request.data
        try:
            proposal_id = data.pop("proposal_id")
            if data:
                loan_application = LoanApplication.objects.create(proposal_id=proposal_id)
                for field_id in data:
                    value = data[field_id]
                    if data:
                        Value.objects.create(loan_application=loan_application, field_id=field_id, value=value)
                proccess_loan_requests.apply_async(countdown=10)
                return Response({"status": "Solicitação criada"})
            else:
                return Response({"status": _("Bad request")}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"status": "error", "message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ValueViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = ValueSerializer
    queryset = Value.objects.all()
