from django import forms

from mailing.models import Mailing, Client


class MailingForm(forms.ModelForm):

    class Meta:
        model = Mailing
        fields = '__all__'  # Включить все поля из модели Рассылки

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['clients'].widget = forms.CheckboxSelectMultiple()  # Используйте флажки для клиентов
        self.fields['clients'].queryset = Client.objects.filter(is_active=True)  # Показывать только активных клиентов