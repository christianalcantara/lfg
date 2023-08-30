from celery import shared_task
from django.db import transaction

from .models import LoanApplication


def update_loans(loan_approveds, loan_dissaproveds, loan_wait):
    approveds = loan_approveds
    dissaproveds = loan_dissaproveds
    ids_approve = []
    ids_disapprove = []
    with transaction.atomic():
        for x in range(loan_wait.count()):
            ag_id = loan_wait[x].id
            if approveds < dissaproveds:
                approveds += 1
                ids_approve.append(ag_id)
            elif dissaproveds < approveds:
                dissaproveds += 1
                ids_disapprove.append(ag_id)
            else:
                approveds += 1
                ids_approve.append(ag_id)
        if ids_approve:
            LoanApplication.objects.filter(id__in=ids_approve).update(approved=True)
        if ids_disapprove:
            LoanApplication.objects.filter(id__in=ids_disapprove).update(approved=False)


@shared_task
def proccess_loan_requests():
    loan_approveds = LoanApplication.objects.filter(approved=True).count()
    loan_dissaproveds = LoanApplication.objects.filter(approved=False).count()
    loan_wait = LoanApplication.objects.filter(approved=None)
    update_loans(loan_approveds, loan_dissaproveds, loan_wait)
    return f"{loan_wait.count()} Loans(s) processed(s)."
