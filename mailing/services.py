# from django.conf import settings
# from django.core.mail import send_mail
#
# from mailing.models import Mailing
#
#
# def send_mailing_email(mailing_item: Mailing):
#     mailing_item.update_status()  # Обновление статуса рассылок перед отправкой
#     clients = mailing_item.clients.all()
#     for client in clients:
#         send_mail(
#             subject=f'{mailing_item.message.title}',
#             message=f'{mailing_item.message.message}',
#             from_email=settings.EMAIL_HOST_USER,
#
#             recipient_list=[client.email],
#             fail_silently=False
#         )
#
#
#         print(f"Client Name: {client.first_name} {client.last_name}, Email: {client.email}")
#
#     running_mailings = Mailing.objects.filter(status=Mailing.Status.RUNNING)  # Выборка рассылок со статусом RUNNING
#     print(running_mailings)
import logging
from config import settings

from django.core.mail import send_mail
from mailing.models import Mailing, Attempt

logger = logging.getLogger(__name__)


def send_mailing_email(mailing_id: int) -> None:
    logger.info('Выполнение рассылки с id %s', mailing_id)
    mailing = Mailing.objects.get(id=mailing_id)

    recipient_list = mailing.clients.values_list('email', flat=True)

    from smtplib import SMTPException
    try:

        sending_mail = send_mail(
            subject=mailing.message.title,
            message=mailing.message.message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=recipient_list,
            fail_silently=False,
        )
    except SMTPException as e:
        mailing.attempts.create(status=Attempt.Status.FAILURE, server_response=str(e))
    else:
        mailing.attempts.create(status=Attempt.Status.SUCCESS if sending_mail else Attempt.Status.FAILURE)

