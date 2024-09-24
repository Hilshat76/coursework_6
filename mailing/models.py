from django.db import models


NULLABLE = {'blank': True, 'null': False}

PERIODICITY_CHOICES = [
    ('once', 'Однократно'),
    ('daily', 'Ежедневно'),
    ('weekly', 'Еженедельно'),
    ('monthly', 'Ежемесячно'),
    ('yearly', 'Ежегодно'),
]

STATUS_MAILING = {
    ('create', 'Создана'),
    ('launched', 'Запущена'),
    ('completed', 'Завершена'),
}


class Client(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    third_name = models.CharField(max_length=50, verbose_name='Отчество', **NULLABLE)
    email = models.EmailField(verbose_name="Электронной почты",unique=True)
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.third_name}: {self.email}'


    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Message(models.Model):
    title = models.CharField(max_length=100, verbose_name="Тема сообщения")
    message = models.TextField(verbose_name="Сообщение")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания", **NULLABLE)

    def __str__(self):
        return f'{self.title} от {self.created_at}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Mailing(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название рассылки")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name="Сообщение", **NULLABLE)
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания", **NULLABLE)
    clients = models.ManyToManyField(Client, verbose_name="Список клиентов", blank=True)
    at_start = models.DateTimeField(verbose_name='Дата и время начала отправки')
    at_end = models.DateTimeField(verbose_name='Дата и время окончания отправки')
    periodicity = models.CharField(max_length=20, choices=PERIODICITY_CHOICES, verbose_name='Периодичность')
    status = models.CharField(max_length=20, verbose_name="Статус рассылки", choices=STATUS_MAILING)

    def __str__(self):
        return f'Рассылка: {self.title} от {self.created_at},  количество клиентов - {self.clients.count()} чел. (статус - {self.status})'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class Attempt(models.Model):
    at_last_attempt = models.DateTimeField(verbose_name='Дата последней попытки', auto_now_add=True)
    status_attempt = models.BooleanField(verbose_name='Статус попытки', default=False)
    answer_mail = models.TextField(verbose_name='Ответ почтового сервера', **NULLABLE)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка', **NULLABLE)

    def __str__(self):
        return f'Попытка отправки'

    class Meta:
        verbose_name = 'Попытка'
        verbose_name_plural = 'Попытки'

