from celery import shared_task
from celery.utils.log import logger, task_logger

from apps.core.loan_processor import evaluate_loan
from apps.proposal.choices import LoanStatus
from apps.proposal.models import LoanApplication


@shared_task()
def proccess_loan_requests():
    loans = LoanApplication.objects.filter(status=None)
    for loan in loans:
        task_logger.debug(loan)
        try:
            response = evaluate_loan(document=loan.partner_document, name=loan.partner_name)
            status = LoanStatus.WAITING_FOR_APPROVAL if response["approved"] else LoanStatus.NOT_APPROVED
            loan.status = status
            loan.save()
        except Exception as e:
            logger.error(e)
            continue
