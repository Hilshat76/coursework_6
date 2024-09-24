from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from mailing.apps import MailingConfig

app_name = MailingConfig.name

urlpatterns = [


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)