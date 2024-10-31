# Generated by Django 5.1.1 on 2024-10-23 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Attempt",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "at_last_attempt",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата последней попытки"
                    ),
                ),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[(1, "Успешно"), (2, "Неудачно")],
                        verbose_name="Статус попытки",
                    ),
                ),
                (
                    "server_response",
                    models.TextField(
                        blank=True, default="", verbose_name="Ответ почтового сервера"
                    ),
                ),
            ],
            options={
                "ordering": ["-at_last_attempt"],
            },
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=50, verbose_name="Имя")),
                ("last_name", models.CharField(max_length=50, verbose_name="Фамилия")),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="Электронной почты"
                    ),
                ),
                ("comment", models.TextField(blank=True, verbose_name="Комментарий")),
            ],
            options={
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
            },
        ),
        migrations.CreateModel(
            name="Mailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Название рассылки"),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True, upload_to="mailing/preview", verbose_name="Превью"
                    ),
                ),
                (
                    "created_at",
                    models.DateField(auto_now_add=True, verbose_name="Дата создания"),
                ),
                (
                    "at_start",
                    models.DateTimeField(verbose_name="Дата и время начала отправки"),
                ),
                (
                    "at_end",
                    models.DateTimeField(
                        verbose_name="Дата и время окончания отправки"
                    ),
                ),
                (
                    "periodicity",
                    models.CharField(
                        choices=[
                            ("C", "Custom"),
                            ("D", "Ежедневно"),
                            ("W", "Еженедельно"),
                            ("M", "Ежемесячно"),
                        ],
                        max_length=1,
                        verbose_name="Периодичность",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("C", "Создана"),
                            ("R", "Запущена"),
                            ("F", "Завершена"),
                        ],
                        default="C",
                        max_length=1,
                        verbose_name="Статус рассылки",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=100, verbose_name="Тема сообщения"),
                ),
                ("message", models.TextField(verbose_name="Сообщение")),
                (
                    "preview",
                    models.ImageField(
                        blank=True, upload_to="message/preview", verbose_name="Превью"
                    ),
                ),
                (
                    "created_at",
                    models.DateField(auto_now_add=True, verbose_name="Дата создания"),
                ),
            ],
            options={
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
            },
        ),
    ]
