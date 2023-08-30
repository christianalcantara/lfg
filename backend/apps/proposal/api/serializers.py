from rest_framework import serializers

from ..models import Field, LoanApplication, Proposal, Value


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ["id", "name", "label", "field_type", "required"]


class ProposalSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True, read_only=True)

    class Meta:
        model = Proposal
        fields = ["id", "name", "fields"]


class ValuesLoanApplicationSerializer(serializers.ModelSerializer):
    field = serializers.SlugRelatedField(many=False, slug_field="label", read_only=True)

    class Meta:
        model = Value
        fields = ["field", "value"]


class LoanApplicationSerializer(serializers.ModelSerializer):
    proposal = serializers.SlugRelatedField(many=False, slug_field="name", read_only=True)
    values_loan_applicattions = ValuesLoanApplicationSerializer(many=True, read_only=True)

    class Meta:
        model = LoanApplication
        fields = ["id", "proposal", "values_loan_applicattions"]


class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ["id", "loan_application", "field", "value"]
